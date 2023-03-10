from pymongo import MongoClient
from bson.objectid import ObjectId

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    name = input("Anna listan nimi: ")
    choice = input("Haluatko nähdä kaikki tehtävät(a), tekemättömät(n) vai tehdyt(d)? ")

    list = db.lists.find_one({'name': name})

    if list is None:
        raise Exception("List not found")
    
    list_id = ObjectId(list['_id'])

    print(list['name'])

    # Check task based on input choice
    # Find all tasks
    if choice == "a":          
        items = db.items.find({'lists_id': list_id})     
        for item in items:
            print(item['task'], item['state'])

    # Find undone tasks
    elif choice == "n":
        items = db.items.find({'lists_id': list_id, 'state': False})
        for item in items:
            print(item['task'])

    # Find done tasks
    elif choice == "d" or "D":
        items = db.items.find({'lists_id': list_id, 'state': {'$ne': False}}) 
        for item in items:
            print(item['task'])   
    

except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()