from pymongo import MongoClient

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    name = input("Anna poistettavan listan nimi: ")
    res = db.lists.delete_one({'name': name})

    if res.deleted_count == 0:
        raise Exception("Listaa ei löytynyt")    

    
except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()