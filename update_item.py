from pymongo import MongoClient
from bson.objectid import ObjectId

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    _id = input("Anna päivitettävän listan id: ")
    res = db.items.update_one({'_id': ObjectId(_id)}, {'$set': {'state': True}})

    if res is None:
        raise Exception("Listaa ei löytynyt")  

    
except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()