from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = os.getenv('DB_URI')
client = MongoClient(DB_URI)

DB_NAME = os.getenv('DB_NAME')
database = client.get_database(DB_NAME)

USER_COLLECTION_NAME = os.getenv('USER_COLLECTION_NAME')

if not database.get_collection(USER_COLLECTION_NAME):
    try:
        user_collection = database.create_collection(USER_COLLECTION_NAME)
    except Exception as error:
        raise error

else:
    user_collection = database.get_collection(USER_COLLECTION_NAME)

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
    user_document = {
        'username': username,
        'password': password,
        'email': email,
    }

    for attr, value in attrDict:
        user_document[attr] = value
    
    
    user = user_collection.insert_one(user_document)
    user_id = None

    if user:
        user_id = user.inserted_id

    return user_id

joao = create_user(
    username='joao', 
    password='password@123456', 
    email='abc@example.com', 
    attrDict={
        'sobre_mim': 'Me chamo Joao Ferreiro, tenho 19 anos e trabalho com programação. Atualmente estudo: python, javascript, c, c++, c#, java ... etc'
})