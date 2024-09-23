from flask import Flask, render_template, redirect, request, flash
import json
app  = Flask(__name__)
app.config['SECRET_KEY'] = '060506'
#rota do formulario

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/adm')





@app.route('/login', methods =[ 'POST'])
def login():
    
    nome = request.form.get('nome')
    senha= request.form.get('senha')

    with open('usuarios.json') as usuarios_cadastrados:
        usuarios = json.load(usuarios_cadastrados)
        cont = 0
        for usuario in usuarios:
            cont += 1
            if nome == "luanadm" and senha == "1234":
                return render_template('administrador.html')
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html')
            
            if cont >= (len(usuarios)):
                flash('USUARIO INVALIDO')
                return redirect("/")
   







































if __name__ in "__main__":
    app.run(debug = True)