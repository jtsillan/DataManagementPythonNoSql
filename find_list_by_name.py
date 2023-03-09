from pymongo import MongoClient
from bson.objectid import ObjectId

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    name = input("Anna listan nimi: ")

    list = db.lists.find_one({'name': name})

    if list is None:
        raise Exception("List not found")    

    print(list['name'])

except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()