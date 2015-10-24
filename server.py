from bottle import BaseTemplate, template, route, run, request, redirect, static_file, response, app, hook, error
from modules.frequency import str_frequency, cache_update, top_twenty, users_cache_update
# oauth/google apis authorization dependencies
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
# http client to get user's information using access code
import httplib2

# session middleware to handle authenticated state
from beaker.middleware import SessionMiddleware
session_opts = {
	'session.type': 'memory',
    'session.cookie_expires': False,
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

# key: word from a query
# val: frequency of word appearing in queries
cache = dict()
# key: user's email,
# val: a list of their last 10 queries
users_cache = dict()


# hook before a request is processed
@hook('before_request')
def update_auth_state():
	# only authenticated users can hit these urls
	restricted_urls = ['/logout','/most-searched']
	# state vars
	s = request.environ.get('beaker.session')
	logged_in = True if (s) and ('user_data' in s) and (s['auth']) else False
	# save path url here
	BaseTemplate.defaults['path'] = request.path

	if (request.path in restricted_urls) and (logged_in == False):
		return redirect('/')
	else:
		BaseTemplate.defaults['session'] = s
		BaseTemplate.defaults['logged_in'] = logged_in
		return


@route('/', method='GET')
def query(results=None):
		s = request.environ.get('beaker.session')
		query = request.query.get('keywords')
		# view rendering control based on whether
		# the keywords parameter is passed in
		if (query):
			last_ten = None
			query_freq = str_frequency(query)
			cache_update(query, cache)
			if ('user_data' in s) and (s['auth']):
				users_cache_update(query, users_cache, s['user_data']['email'])
				last_ten = users_cache[s['user_data']['email']]
			return template('views/results.tpl', results=query_freq, query_str=query, last_ten=last_ten)
		else:
			return template('views/landing.tpl')

# oauth endpoint
@route('/auth/google', method='GET')
def authorize():
	s = request.environ.get('beaker.session')

	# check if authorized
	if ('auth' in s):
		s['auth'] = True
		s.save()
		return redirect('/')

	flow = flow_from_clientsecrets('client_secrets.json',
									scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email',
									redirect_uri='http://localhost:8080/auth/google')
	auth_uri = flow.step1_get_authorize_url()
	code = request.query.get('code')
	if (code):
		credentials = flow.step2_exchange(code)
		# unpack credentials and stash in session
		http = httplib2.Http()
		http = credentials.authorize(http)

		user_service = build('oauth2', 'v2', http=http)
		user_data = user_service.userinfo().get().execute()

		s['user_data'] = user_data
		s['auth'] = True
		s.save()

		return redirect('/')
	else:
		return redirect(auth_uri)


@route('/most-searched', method='GET')
def most_searched(results=None):
	# grab the top twenty results
	results = top_twenty(cache)
	return template('views/most-searched.tpl', results=results)

@route('/logout', method='GET')
def logout():
	s = request.environ.get('beaker.session')
	s['auth'] = False
	s.save()
	return redirect('/')

# to serve all static assets - images, CSS and JS
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run (host='localhost',port=8080, debug=True, app=app)
