import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-irprk.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.test

mydb = client['mydatabase']
mycol = mydb["students"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)

print("\n")
myquery1 = { "address": { "$regex": "^S" } }
newvalues1 = { "$set": { "name": "Minnie" } }

h = mycol.update_many(myquery1, newvalues1)

print(h.modified_count, "documents updated.")

myresult = mycol.find().limit(5)

print("\n")
for l in myresult:
  print(l)