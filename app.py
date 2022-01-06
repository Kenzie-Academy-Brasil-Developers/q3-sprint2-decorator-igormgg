from flask import Flask, request, jsonify
from werkzeug.wrappers import response
from decorators import verify_credentials, verify_username

from helpers import find_users


app = Flask(__name__)

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# Desenvolva suas rotas abaixo

@app.get('/')
def test():
    user_data = find_users()
    return jsonify(user_data)

@app.post('/login')
@verify_credentials
def login():
    return {"msg": f"Bem vindo {request.json['username']}"}, 200


@app.post('/register')
@verify_username
def register():
    return {"msg": f"Usuário {request.json['username']} criado com sucesso!"}, 201