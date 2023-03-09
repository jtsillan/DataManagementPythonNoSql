from pymongo import MongoClient

client = None
db = None

try:
    client = MongoClient('localhost', 27017)
    db = client.MongoDB_tehtava

    name = input("Anna luotavan listan nimi: ")

    check_res = db.lists.find_one({'name': name})

    if check_res is not None:
        raise Exception("Lista on jo olemassa, käytä toista nimeä")

    db.lists.insert_one({'name': name})

except Exception as ex:
    print(ex)

finally:
    if client is not None:
        client.close()