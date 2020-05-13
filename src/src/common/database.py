_author_='Dibya Ganguly'

import pymongo


class Database(object):
    #URI="mongodb://127.0.0.1:27017"  172.21.107.87
    URI = "mongodb://root:root@mongo:27017/kalptreedb"
    DATABASE= None

    @staticmethod
    def inttialize():
        client=pymongo.MongoClient(Database.URI)
        Database.DATABASE=client['fullstack']
    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
       return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
       return Database.DATABASE[collection].find_one(query)