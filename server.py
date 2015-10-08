from bottle import route, run, template, request, redirect
from modules.frequency import str_frequency

@route('/')
def index():
	redirect('/query')

@route('/query', method='POST')
def query():
		query = request.forms.get('query')
		query_freq = str_frequency(query)
		return template('views/index.tpl',results=query_freq)

@route('/query', method='GET')
def query(results=None):
		return template('views/index.tpl',results=None)

run (host='localhost',port=3000, debug=True)
