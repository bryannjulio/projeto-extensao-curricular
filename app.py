from flask import Flask, render_template, request
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home/index.html')



@app.route('/<template>')
def show_template(template):
    print('teste rotas'+template)
    try:
        return render_template( 'home/' + template )
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

@app.route('/contact_us.hmtl', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        whatsapp = request.form['whatsapp']
        
        # Aqui você pode salvar os dados no banco de dados ou fazer qualquer outra ação necessária
        # Por exemplo, você pode usar um ORM como SQLAlchemy para salvar no banco de dados
        
        # Retornar uma mensagem de sucesso
        return "Formulário enviado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
