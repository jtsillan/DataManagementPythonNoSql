from pymongo import MongoClient
from bson.objectid import ObjectId

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    list_name = input("Mihin listaan haluat lisätä tehtävän? ")
    task_name = input("Anna tehtävän nimi: ")

    list = db.lists.find_one({'name': list_name})

    if list is None:
        raise Exception("List not found")    
    
    list_id = ObjectId(list['_id'])

    db.items.insert_one({'task': task_name, 'state': False, 'lists_id': list_id}) 

except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()