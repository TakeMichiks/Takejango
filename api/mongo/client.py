from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

mongo = os.getenv("MONGO_URL")

client = MongoClient(mongo)

# Elegir base de datos y colección
db = client["BaseAndresEloy"]
# collecion de Users 
collection = db["Users"]
# Collecion Stundents
collectionStudents = db["Students"]
# Collecion de Teachers
collectionTeachers = db["Teachers"]
