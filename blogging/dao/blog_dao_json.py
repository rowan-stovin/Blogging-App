from blogging.dao.blog_dao import BlogDAO

class BlogDAOJSON(BlogDAO):
	def __init__(self):
		self.blogs = {}
	
	def search_blog(self, key):
		pass	

	def create_blog(self, blog):
		pass	

	def retrieve_blogs(self, search_string):
		pass

	def update_blog(self, key, blog):
		pass

	def delete_blog(self, key):
		pass

	def list_blogs(self):
		pass