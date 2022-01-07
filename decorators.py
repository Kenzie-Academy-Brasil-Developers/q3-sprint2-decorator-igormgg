# Desenvolva seus decorators aqui
from flask import request
from functools import wraps
from helpers import find_users, write_user

def verify_keys(trusted_keys: list[str]):
    def middleFunction(func):
        @wraps(func)
        def innerFunction():
            requirement = request.json
            username = trusted_keys[0]
            password = trusted_keys[1]
            
            try:
                requirement[username]
                requirement[password]
                return func()
            
            except KeyError:
                return {
                    "error": "chave(s) incorreta(s)",
                    "expected": [
                        "username",
                        "password"
                    ],
                    "received": list(requirement.keys())
                }, 400

        return innerFunction

    return middleFunction


def verify_credentials(func):
    def inner():
        requirement = request.json
        user_data = find_users()

        for user in user_data:
            if requirement['username'] == user['username'] and requirement['password'] == user['password']:
                return func()
        
        return {"error": "not authorized"}, 401
    
    return inner
            
def verify_username(func):
    def innerFunc():
        requirement = request.json
        user_data = find_users()

        for user in user_data:
            if requirement['username'] == user['username']:
                return {"error": "usuario já cadastrado!"}, 422
        
        write_user()
        return func()

    return innerFunc