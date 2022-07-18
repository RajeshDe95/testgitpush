import pymongo
client = pymongo.MongoClient("mongodb+srv://rajesh:rajesh123@raj95.c0ymy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client[ 'mongotest']
coll = db1['test']
coll.insert_one(d)