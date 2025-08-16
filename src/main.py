from pymongo import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
from os import getenv

load_dotenv()

uri = getenv("uri")
db = getenv("DB")

client = MongoClient(uri)

#db = client.get_database("DB")
#users = db.get_collection("users")