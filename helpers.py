# Desenvolva sua funções auxiliares para processamento de arquivo txt aqui
from flask import request
from os import getenv

FILENAME = getenv("DATABASE_FILENAME")

def find_users():
    try:
        with open(f'./{FILENAME}', 'r') as f:
            users = f.read()
            user_data_arr = users.split('\n')
            user_data = []

            for user in user_data_arr:
                user_arr = user.split(':')
                register = {'username': user_arr[0], 'password': user_arr[1]}
                user_data.append(register)
                
            return user_data
    except FileNotFoundError:
        return 'Not found', 404

def write_user():
    try:
        with open(f'./{FILENAME}', 'a') as f:
            requirement = request.json
            user_to_register = f'\n{requirement["username"]}:{requirement["password"]}'
            f.write(user_to_register)

            return 'User registered', 201

    except FileNotFoundError:
        return 'Not found', 404