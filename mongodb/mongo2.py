import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-irprk.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.test

mydb = client['mydatabase']
mycol = mydb["students"]
x = mycol.find_one()
print(x)

print("\n")
students = mycol.find()
for y in students :
    print(y)

print("\n")
for z in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(z)

print("\n")
for a in mycol.find({},{ "address": 0 }):
    print(a)

print("\n")

query = {"name" : "Aruzhan"}
students1 = mycol.find(query)
for b in students1 : 
    print(b)

print("\n")
query1 = {"address" : {"$gt": "S"}}
students2 = mycol.find(query1)
for d in students2 :
    print(d)

print("\n")
query2 = {"address" : {"$regex" : "^S"}}
students3 = mycol.find(query2)
for t in students3:
    print(t)


