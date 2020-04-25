import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-irprk.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.test

mydb = client['mydatabase']
mycol = mydb["students"]

students = mycol.find().sort("name")
for x in students :
    print(x)

print("\n")
students1 = mycol.find().sort("name", -1)
for y in students1 :
    print(y)

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

print("\n")
for z in mycol.find():
    print(z)


