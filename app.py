from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)
filipe = 0
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


if __name__ == '__main__':
    app.run(debug=True)
