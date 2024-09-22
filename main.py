from flask import Flask, render_template, redirect, request, flash

app  = Flask(__name__)
app.config['SECRET_KEY'] = '060506'
#rota do formulario

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login', methods =[ 'POST'])
def login():
    #dados que vou salvar do login
    nome = request.form.get('nome')
    #nome que vitor escolher
    senha= request.form.get('senha')
    if (nome =='luan' and senha =='1234') or( nome =="victor" and senha =='1234'):
        return render_template("usuario.html")
    else:
        flash("USUARIO INVALIDO")
        return redirect("/")







































if __name__ in "__main__":
    app.run(debug = True)