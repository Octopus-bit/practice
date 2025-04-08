from pymongo import MongoClient

client = MongoClient()
db = client.testdb
users_collection = db.users

new_user = {                         
    "name": "ali",
    "age": 22,
    "city": "new york"
}

users_collection.insert_one(new_user) # create

users = users_collection.find() #read
for user in users:
    print (user)

users_collection.update_one({"name": "ali"}, {"$set": {"age": 21}}) #update
print(f"updated user info: {user["age"]}")

users_collection.delete_one({"name": "ali"}) #delete

client.close()

