import streamlit
from pymongo import MongoClient

URI = "mongodb://localhost:27017"

mongodb_client = MongoClient(URI)
DB_CONFIG= mongodb_client["Proj_Config"]


def get_client():
    return mongodb_client

# Create Db Projet
def create_DB(db_name):
    dbs = mongodb_client.list_database_names()
    if db_name in dbs:
        print(f"{db_name} already exists.")
        drop_collections(db_name)

    database = mongodb_client[db_name]
    return database

# Create Schem
def create_schema(database, data):
    request = database['schema'].insert_many(data)
    try:
        request
    except Exception as err:
        print(f'erreur : {err}')

    return database['schema']


# Create collection
def create_collection(database, collection, data):
    request = database[f'{collection}'].insert_many(data.to_dict("records"))
    try:
        request
    except Exception as err:
        print(f'erreur : {err}')

# Drop existing collections
def drop_collections(db):
    collections = mongodb_client[db].list_collection_names()
    for collection in collections:
        try:
            mongodb_client[db][f'{collection}'].drop()
        except Exception as err:
            print(f'erreur : {err}')

# Drop collection in a specific database
def drop_collection(db, collection):
    db[f'{collection}'].drop()

# Get collection in a specific database
def get_collection(db, collection):
    nb_elements = db['schema'].count_documents({})
    if nb_elements > 0:
        data = db[f'{collection}'].find()
        return data

    return False

def get_nb_elem(db, collection, query=None):
    if query is None:
        query = {}
    nb_elements = db[f'{collection}'].count_documents(query)
    return nb_elements

# Get collections
def get_collections(db):
    collections = db.list_collection_names()
    return collections

# Get Projects
def get_projects():
    dbs = [col for col in mongodb_client.list_database_names() if col.startswith('Project_')]
    return dbs