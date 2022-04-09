import random

from flask import Flask, render_template, request, redirect, abort
from models import db, PasswordModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


def generate_password():
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    upper_symbols = symbols.upper()
    chars = list()
    chars.extend(symbols)
    chars.extend(upper_symbols)
    chars.extend('-()[]!@#$')
    chars.extend('0123456789')

    generated_password = ''
    random_length = random.randint(8, 15)
    for i in range(random_length):
        generated_password += random.choice(chars)

    return generated_password


@app.route('/')
def index():
    return generate_password()


@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create_page.html')

    if request.method == 'POST':
        password_id = request.form['password_id']
        site = request.form['site']
        login = request.form['login']
        gen_password = generate_password()
        password_model = PasswordModel(password_id=password_id, site=site, login=login, password=gen_password)
        db.session.add(password_model)
        db.session.commit()
        return redirect('/data')


@app.route('/data')
def RetrieveList():
    site_login_passwords = PasswordModel.query.all()
    return render_template('datalist.html', passwords=site_login_passwords)


@app.route('/data/<int:id>')
def RetrievePassword(id):
    password = PasswordModel.query.filter_by(password_id=id).first()
    if password:
        return render_template('data.html', password=password)
    return f"password with id ={id} Doesnt exist."


@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    password = PasswordModel.query.filter_by(password_id=id).first()
    if request.method == 'POST':
        if password:
            db.session.delete(password)
            db.session.commit()

            site = request.form['site']
            login = request.form['login']
            password = request.form['password']
            password = PasswordModel(password_id=id, site=site, login=login, password=password)

            db.session.add(password)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Password with id = {id} Does nit exist"

    return render_template('update.html', password=password)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    password = PasswordModel.query.filter_by(password_id=id).first()
    if request.method == 'POST':
        if password:
            db.session.delete(password)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete.html')


app.run(host='localhost', port=5000)
