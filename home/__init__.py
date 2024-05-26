from flask import Blueprint

# Nomeie seu blueprint aqui
blueprint = Blueprint(
    'home_blueprint',
    __name__,
    template_folder='templates',  # Definir o diretório de templates
    static_folder='static'        # Definir o diretório de arquivos estáticos (opcional)
)

# Importe as rotas após definir o blueprint para evitar ciclos de importação
from . import routes
