from pymongo import MongoClient

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    lists = db.lists.find()

    for list in lists:
        print(list['name'])

except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()