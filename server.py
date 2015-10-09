from bottle import route, run, template, request, redirect, static_file
from modules.frequency import str_frequency, cache_update, top_twenty

# dictionary to store all searched words,
# and their frequencies
cache = dict()

@route('/', method='GET')
def query(results=None):
		query = request.query.get('keywords')
		# if the keywords URL parameter is sent
		# load the landing page, if not,
		# load with computed count
		if (query):
			query_freq = str_frequency(query)
			cache_update(query, cache)
			return template('views/results.tpl',results=query_freq, query_str=query)
		else:
			return template('views/landing.tpl')

@route('/most-searched', method='GET')
def most_searched(results=None):
	# grab the top twenty results
	results = top_twenty(cache)
	return template('views/most-searched.tpl', results=results)


# to serve all static assets - images, CSS and JS
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run (host='localhost',port=3000, debug=True)
