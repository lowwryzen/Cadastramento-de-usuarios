from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sys

load_dotenv()

DB_URI = os.getenv('DB_URI')
print(DB_URI)
client = MongoClient(DB_URI)

DB_NAME = os.getenv('DB_NAME')
database = client.get_database(DB_NAME)

USER_COLLECTION_NAME = os.getenv('USER_COLLECTION_NAME')

try:
    user_collection = database.get_collection(USER_COLLECTION_NAME)
except:
    user_collection = database.create_collection(USER_COLLECTION_NAME)

def create_user(username: str, password: str, email: str = None, attrDict: dict = None):
    """Cria um usuario apartir de alguns dados e o retorna da função.

    Argumentos:
        username(texto): Nome de usuario. -> Obrigatorio 
        password: Senha do usuario. -> Obrigatorio
        email: Email do usuario. -> Opcional
        attrDict: Dicionario de atributos. -> Opcional
    
    Retornos:
        ID do usuario para identificação posterior. OBS: se retornar 'None' significa que não foi possivel criar
    """

    result = {
        'id': None,
        'error': None
    }

    user_document = {
        'username': username,
        'password': password,
        'email': email
    }

    for attr, value in attrDict.items():
        user_document[attr] = value

    error_msg = "Houve um erro ao tentar criar o usuario: "

    find_user_result = user_collection.find_one({'username': username})
    if find_user_result:
        result['id'] = find_user_result.get('_id')
        result['error'] = f"O usuario '{username}' já existe no MongoDB!"
    else:
        try:
            insert_result = user_collection.insert_one(user_document)
            if insert_result.inserted_id:
                return insert_result.inserted_id
        except Exception as error:
            result['error'] = error

    return result

def find_user(username: str):
    """Tenta encontrar o usuario na na coleção de usuarios da Database do MongoDB

    Argumentos:
        username(texto): Nome do usuario
    
    Retornos:
        Dicionario contendo as informações do usuario | Ou 'None'. Simbolizando que não foi possivel encontrar o usuario 'x'.
    """
    return user_collection.find_one({'username': username})