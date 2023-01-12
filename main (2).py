#flask precisa da pasta templates para rodar o html, em qqr lugar que eu programar
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/') #pag inicial: carrega ao entrar no sistema
def pag_inicial():
  return render_template('inicio.html') 

@app.route('/entrar/')
def admin_index():
  return render_template('login.html') #carrega a tela p fazer login 

@app.route('/login/', methods=['POST', 'GET']) #efetua o teste que a rota entrar forneceu, redirecionando p rota admin ou se acesso errado ele direciona para entrar dnv
def login():
  if request.method == 'POST': 
    usuario=request.form['c_usuario']
    senha=request.form['c_senha']
    if usuario == "lorena" and senha == "lorena":
      return redirect(url_for('admin', nome=usuario, senha=senha)) # indo para a rota admin
    else:
      return redirect(url_for('entrar'))
  else:
    usuario=request.args.get('c_usuario')
    senha=request.args.get('c_senha')
    if usuario == "lorena" and senha == "lorena":
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      return redirect(url_for('entrar'))
      
@app.route('/admin/<nome>/<senha>') #rota p usuarios logados, chega aq dps de percorrer a rota de login anterior e o acesso for concedido
def admin(nome, senha):
  frase="<b> bem vindo </b>" + nome + "a senha e: <i>" + senha + "</i>" 
  # b negrito i italico
  return frase
  
if __name__ == '__main__':
  app.run('0.0.0.0') 
#ou '127.0.0.1': local host