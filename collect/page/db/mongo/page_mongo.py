from pymongo import MongoClient as mc

#TODO: create a method that will give back a list of keys inside of a dictionary

class page_mongo(object):
	"""
	A database connection to mongodb for page
	"""
	def __init__(self,db,host='localhost',port=27017):
		self.client = mc(host,port)
		self.host = host
		self.port = port
		self.db = self.client[db]
		self.collection = self.db[db]
#		try:
#			self.client = mc(port,host)
#			self.host = host
#			self.port = port
#			self.db = self.client[db]
#			self.collection = self.db[db]
#		except:
#			# TODO: inform of a bad connection diagnose problem and return the error.
#			pass

	def insert(self, data):
		""" insert data into the given collection """
		# TODO: need to create a method that guarentees that the data being passed in is valid.
		self.collection.insert(data)

	def search(self,arg={}):
		# NOTE: pymongo accepts dictionary data. i dont think that you can pass in an empty string like you can in the `mongo` client
		try:
			results = [item for item in self.collection.find(arg)]
#			results = []
#			for item in self.collection.find(arg):
#				results.append(item)
		except:
			# TODO: create an exception for incorrect argument passed into search then show examples of proper arguments for this function.
			print('The argument that you supplied was not valid')

if __name__ == "__main__":
	import sys
	d = {"hello":"world!!!",does_it:"work"}
