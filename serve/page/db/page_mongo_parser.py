"""
a class that is used to query mongo and return data in a more structured format
for example you could ask for all the paragraphs returned from an html page
"""
import BeautifulSoup as bsp
from pymongo import MongoClient as mc

__author__ = "Alex Balzer <abalzer22@gmail.com>"
__version__ = "0.1.0"

class page_mongo_search(object):
	"""  """
	def __init__(self):
