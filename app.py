from urllib import response
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask import Flask, session, redirect, g
from flask import request,flash
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.evento_blueprint import evento_blueprint
from backend.blueprints.ponente_blueprint import ponente_blueprint
app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"

app.register_blueprint(evento_blueprint)
app.register_blueprint(ponente_blueprint)

cors = CORS(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', eventos=response)


@app.route('/home', methods=['GET','POST'])
def home():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    return render_template('home.html', eventos=response)
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate_login', methods = ['POST'])
def validate_login():
    if request.method == 'POST':
        correo = request.form['typeEmailX']
        password = request.form['typePasswordX']
        
        users=requests.post("http://127.0.0.1:5000/api/ponente/get_all").json()
        user={}
        for x in users:
            if x['correo']==correo:
                user=x
                break
        if not user:
            return "Not found"
        elif password == user['nombre']:
            session['correo'] = user['correo']
            return  redirect(url_for('home'))

    return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/logout')
def logout():
    if 'correo' in session:
        session.pop('correo', None)
        return render_template('index.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombres = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        query= {'id_ponente' : 2,
        'nombres' : nombres,
        'apellidos' : apellidos,
        'email' : email}
        requests.post("http://127.0.0.1:5000/api/asistente/create",json=query)
        return render_template('home.html')
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    return render_template('evento.html', evento=resp)


@app.route('/create_evento', methods=['GET','POST'])
def create_evento():
    if request.method == 'POST':
        query= {
        'id_ponente' : 2,
        'nombre' : request.form['evento_nombre'],
        'detalles' : request.form['evento_detalles'],
        'link' : request.form['evento_link']}
        requests.post("http://127.0.0.1:5000/api/evento/create",json=query)
        return  redirect('/home')
    return render_template('create_evento.html')


@app.route('/profile/<int:id>', methods=['GET'])
def profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

@app.route('/edit_evento/<int:id>', methods=['GET','POST'])
def edit_evento(id):
    if request.method == 'POST':
        query= {
        'id' : id,
        'id_ponente' : 2,
        'nombre' : request.form['evento_nombre'],
        'detalles' : request.form['evento_detalles'],
        'link' : request.form['evento_link']}
        requests.post("http://127.0.0.1:5000/api/evento/edit",json=query)
        return  redirect('/home')

    return render_template('edit_evento.html')


@app.route('/delete_evento/<int:id>', methods=['GET','POST'])
def delete_evento(id):
    print(id)
    query = {"id" : id}
    requests.post("http://127.0.0.1:5000/api/evento/delete", json=query)
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True)
