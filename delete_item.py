from pymongo import MongoClient
from bson.objectid import ObjectId

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    _id = input("Anna poistettavan tehtävän id: ")
    res = db.items.delete_one({'_id': ObjectId(_id)})

    if res.deleted_count == 0:
        # PALAUTE no nyt on siistiä virheenkäsittelyä :)
        raise Exception("Listaa ei löytynyt")  

    
except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()