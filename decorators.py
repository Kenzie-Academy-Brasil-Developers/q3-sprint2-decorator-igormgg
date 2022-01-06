# Desenvolva seus decorators aqui
from flask import request

from helpers import find_users, write_user

# verify_keys(trusted_keys: list[str])


# def verify_credentials(func):
#     def inner():
#         response = request.json
#         user_data = find_users()

#         for user in user_data:
#             if response['username'] == user['username'] and response['password'] == user['password']:
#                 return func()
        
#         return {"error": "not authorized"}, 401
    
#     return inner

def verify_credentials(func):
    def inner():
        response = request.json
        user_data = find_users()

        for user in user_data:
            if not response['username'] == user['username'] and response['password'] == user['password']:
                return {"error": "not authorized"}, 401
        
        return func()
    
    return inner
            
def verify_username(func):
    def innerFunc():
        response = request.json
        user_data = find_users()

        for user in user_data:
            if response['username'] == user['username']:
                return {"error": "usuário já cadastrado!"}, 422
        
        write_user()
        return func()

    return innerFunc