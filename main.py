from my_mongo import MyMongo
from bson.objectid import ObjectId

DB = 'carbon'
COLLECTION =  'carbon_nanotubes'
FILE_NAME = 'carbon_nanotubes.csv'

conn = MyMongo(DB,COLLECTION)

print(conn.db)
print(conn.coll)

#Show existing databases
print(conn.show_databases())

#Selecting all documents form collection
print(conn.select_all_docs())

#Bulk insert fron csv file
conn.insert_from_csv(FILE_NAME)

# Selecting all documents inserted
print(conn.select_all_docs())

# Selecting all documents count from collection
print(len(conn.select_all_docs()))

#Show existing database
print(conn.show_databases())