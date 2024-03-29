# Emily Wood
# CS340
# Client/Server Development
# 11/20/2022

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # init to connect to mongodb without authentication
        #self.client = MongoClient('mongodb://localhost:39113')
        # init connect to mongodb with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:39113/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']

# A method that inserts a document into a specified MongoDB database and collection
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# A method that queries for documents from a specified MongoDB database and specified collection
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False} )
        return cursor

# Create method to implement the R in CRUD.
    def read(self, data):
        return self.database.animals.find_one(data)
