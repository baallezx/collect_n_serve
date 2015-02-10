"""
a basic graph object that handles crawling the web for content using basic graph theory.

Example usage:
$ python page.py http://whatever.com ...

`...` dots represent other url links you can enter in
"""
import db.mongo.page_mongo as pm

__author__ = "Alexander Balzer <abalzer22@gmail.com>"
__version__ = "0.1.3"

diff_hash = {} # if the value is already in the hash then skip it
dbm = pm.page_mongo("bfs_page_crawler")

class page_maker(object):
	"""
	a basic page maker who creates pages with dfs, bfs, 
	or another type of search mechanism
	"""
	def __init__(self,url,search_type="bfs",depth=65536):
		self.pages = {}
		# TODO: make a better queue.. that can be pickled or placed in a database if some error occurs.
		self.q = [] # a queue for breadth first search
		if search_type == "bfs": # do breadth first
			page_one = page(url,depth)
			self.q.append(page_one)
			while self.q:
				curr_page = self.q.pop(0)
				curr_page.children = curr_page.get_child_nodes(curr_page.links)
				# TODO: create a sort method that can better find good links and place them in order.
				for child in curr_page.children:
					self.q.append(child)
		elif search_type == "dfs": # do depth first
			pass
		else: # something non obvious
			print("you need to specify either 'bfs', or 'dfs'")
			return None

# TODO: add timestamp if mongodb does not already do so.
# TODO: create multiple ways to traverse through the web. dfs, bfs, user-picked, random, ...
class page(object):
	"""
	a basic webpage object
	"""
	def __init__(self,url,depth=65536,parent=None):
		if self.check_hash(url) and depth > 0:
			self.url = url #string
			self.parent = parent #string
			self.depth = depth
			print((self.depth,self.url))
			self.data = self.get_page_data(url) #[strings]
			self.links = self.get_links(self.data) # child nodes
			self.children = None #self.get_child_nodes(self.links)
			self.filename = None
			self.update_hash(url)

	def printer(self):
		""" print object to screen """
		print "url = ",self.url,"\n","parent = ",self.parent,"\n","data = ",self.data,"\n","links = ",self.links,"\n","children = ",self.children,"\n","filename = ",self.filename

	def get_page_data(self,url):
		""" get the flat plain text for the current page """
		import urllib2
		try:
			return urllib2.urlopen(url).read()
		except:
			return None

	# TODO: abstract this so that you can get {links: 'a', pics: 'href', ...}
	# TODO: create a recursive method that can get paragraphs inside of body or other element statements, this will allow for deeper digging.
	def get_links(self,data):
		""" get the raw strings of links to the current page """
		import BeautifulSoup as bsp
		try:
			soup = bsp.BeautifulSoup(data)
			return [link['href'] for link in soup.findAll('a',href=True)]
		except:
			return None

	def get_child_nodes(self,links):
		""" take this pages links and create new page objects that will become 'children' nodes. the reason i used quotes is because that could be left to interpretation. the internet does not move in 1 direction. it is a graph not a tree."""
		self.write_data()
		if isinstance(links,list):
			for i in links:
				if isinstance(i,str) or isinstance(i,unicode):
					try:
						new_depth = int(self.depth - 1)
						child = page(i, new_depth, self.url)
						# TODO: add a new entry to whatever database you are using.
					except:
						# TODO: notify you have a failed page. add to some other process to figure out what to do with this link
						pass

# TODO: write a method to handle cleaning up beautiful soup data. like fetch_all(data,node_token) where node_token=['a','p','h1','h2']

	def write_data(self,location=None):
		""" write data to a specified file location. """
		try:
			if location == None:
				location = "/tmp/scoobydoo.x15"
			w = open(location,"a")
			w.write("\n@~@\n")
			w.write(self.url)
			w.write("\n:::\n")
			for i in self.data:
				w.write(i)
			w.write("\n;;;\n")
			w.write(str(self.children))
			w.write("\n~@~\n")
		except:
			pass

	def save_data(self):
		""" save data to a mongodb database. """
		# TODO: add better functionality for this currently it is way to basic but it is good for testing.
		global dbm
		try:
			dbm.insert(self.__dict__)
			# TODO: add remaining database selection and data insertion.
		except:
			# TODO: inform user that the library is not included on the current machine.
			return False

	def check_hash(self, key):
		""" check public hash table for a collision so infinite recursion can be caught """
		global diff_hash
		if key in diff_hash:
			return False
		else:
			diff_hash[key] = 0x00 # TODO: set as a pointer to page(object) -or- database pointer.
			return True

	def update_hash(self, key):
		""" update the hash table with the dcitionary representation of the objects data. """
		global diff_hash
		if key not in diff_hash:
			raise Exception
		else:
			diff_hash[key] = self.__dict__

def dump_hash(filename):
	""" dump the diff_hash to a json file """
	# TODO: add functionality that will only print a max file size, anything after that will be dumped to a new file.
	import json
	global diff_hash
	# TODO: save diff_hash to a json file named filename
	str_hash = unicode(str(diff_hash),errors='replace')
	json_string = json.dumps(diff_hash)
	w = open(filename,'w')
	w.write(json_string)
	w.close()

# [']'|'[']
# |'[']'|'[
# ]'|'[']'|

if __name__ == "__main__":
	import sys
	#l = sys.argv[1:]
	l = []
	n = 0
	for i in l:
		try:
			curr_page = page(i,4)
		except KeyboardInterrupt as ke:
			dump_hash("interrupt.json")
#		else:
#			dump_hash("main.json")
#		print('WTF!!!')
