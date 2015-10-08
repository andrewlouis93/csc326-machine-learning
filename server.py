from bottle import route, run, template, request, redirect, static_file
from modules.frequency import str_frequency

@route('/', method='GET')
def query(results=None):
		query = request.query.get('keywords')
		if (query):
			query_freq = str_frequency(query)
			return template('views/results.tpl',results=query_freq)
		else:
			return template('views/landing.tpl')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run (host='localhost',port=3000, debug=True)
