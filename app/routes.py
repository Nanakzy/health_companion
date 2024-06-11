from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
from flask import current_app as app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        user = User(username=name, email=email)
        db.session.add(user)
        db.session.commit()

        flash('User Added successfully')
        return redirect(url_for('index'))
