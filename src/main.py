from pymongo import MongoClient

from dotenv import load_dotenv
from os import getenv

from database import mongodb

load_dotenv()

uri = getenv("DB_URI")
db = getenv("DB_NAME")

client = MongoClient(uri)

# Código principal #