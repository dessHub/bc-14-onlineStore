from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Put your secret key here'
DB_NAME = 'store'

DATABASE = MongoClient()[DB_NAME]
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True
