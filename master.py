# -*- coding : utf-8 -*-

from flask import Flask, request, flash, url_for, \
    redirect, render_template, session, jsonify
from database import db_master

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

	return ''

if __name__ == '__main__':
    app.run(debug=True)