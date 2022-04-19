from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal collection in MongoDB """
	#Initalizing MongoDB with authentication
	def __init__(self, username, password):
		self.client = MongoClient( 'mongodb://%s:%s@localhost:27017/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
		self.database = self.client['AAC']
	#Creation method
	def create(self, data=None):
		if data is not None:
			self.database.animals.insert(data)
			return True
		else:
			raise Exception("Nothing to save, because data parameter is empty")
        
	#Read method
	def read_all(self, data=None):
		if data:
			cursor = self.database.animals.find(data, {'_id':False}) ## Ignore the ID key/pair values on return
		else: 
			cursor = self.database.animals.find( {} , {"_id":False})
		return cursor
	
	def read(self, data=None):
		return self.database.animals.find_one(data) ## Returns one document

	#Update method
	def update_many(self, filter, update):
		if filter is not None:
			result = self.database.animals.update_many(filter, update)
			return result
		else:
			raise Exception("Nothing to update, because data parameter is empty")

	def update_one(self, filter, update):
		return self.database.animals.update_one(filter, update)

	#Delete method
	def delete_many(self, filter):
		if filter is not None:
			remove = self.database.animals.delete_many(filter)
			return remove
		else:
			raise Exception("Nothing to delete, because data parameter is empty")

	def delete_one(self, filter):
		return self.database.animals.delete_one(filter)