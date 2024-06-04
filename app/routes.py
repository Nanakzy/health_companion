#!/usr/bin/python3

from flask import render_template, request, redirect, url_for, flash
from app import app, mysql


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute
        ("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        flash('User Added successfully')
        return redirect(url_for('index'))
