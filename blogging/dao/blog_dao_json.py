from blogging.dao.blog_dao import BlogDAO
from blogging.blog import Blog

class BlogDAOJSON(BlogDAO):
	def __init__(self):
		self.blogs = {}
		
	
	def search_blog(self, key):
		return self.blogs.get(key)

	def create_blog(self, blog):
		# add a new blog
		self.blogs[blog.id] = blog
		return blog

	def retrieve_blogs(self, search_string):
		retrieved_blogs = []
		for blog in self.blogs.values():
			if search_string in blog.name:
				retrieved_blogs.append(blog)
		return retrieved_blogs

	def update_blog(self, key, blog):
		self.blogs.pop(blog.id)
		blog.id = key
		self.blogs[key] = blog
		return True

	def delete_blog(self, key):
		self.blogs.pop(key)
		return True

	def list_blogs(self):
		blogs_list = []
		for blog in self.blogs.values():
			blogs_list.append(blog)
		return blogs_list