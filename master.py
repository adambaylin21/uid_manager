# -*- coding : utf-8 -*-

from flask import Flask, request, flash, url_for, \
    redirect, render_template, session, jsonify
from database import db_master
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ahihidocho'

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/logic/<mode>', methods=['GET', 'POST'])
def do_logic(mode):
	if mode == 'add_uid':
		uidx = request.form['add_uid']
		uidx = eval(uidx)
		uidx = uidx.splitlines()
		i = 0
		for uid in uidx:
			i += 1
			db_master(mode='add_uid',uid=uid)
		i = '<p id="total_add">Had add {} uid to Database </p>'.format(i)
		return jsonify({'data': i})
	
	if mode == 'del_all':
		db_master(mode='del_all')
		i = '<p id="total_add">Had delete all uid to Database</p>'
		return jsonify({'data': i})

	if mode == 'check_status':
		now = datetime.datetime.now()
		a, b = db_master(mode='max_uid'), db_master(mode='min_uid')
		try:
			c = int(a) - int(b) + 1
		except:
			c = 0
		d = now.strftime("%Y-%m-%d | %H:%M:%S")
		e = """<div class="status_uid">
			<ul id='status_main'>
				<li>Total UID: {}</li>
				<li>Last Update: {}</li>
				<li>Status Nick:</li>
			</ul></div>""".format(c, d)
		return e

	if mode == 'get_uid':
		return str(db_master(mode='get_uid'))

	return ''

if __name__ == '__main__':
    app.run(debug=True)