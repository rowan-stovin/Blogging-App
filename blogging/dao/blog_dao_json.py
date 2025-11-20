from blogging.dao.blog_dao import BlogDAO
from blogging.blog import Blog
from blogging.configuration import Configuration
from blogging.dao.blog_decoder import BlogDecoder
from blogging.dao.blog_encoder import BlogEncoder
import json

class BlogDAOJSON(BlogDAO):
	def __init__(self):
		self.blogs = {}
		self.config = Configuration()
		if self.config.autosave == True:
			try:
				with open(self.config.blogs_file, 'r') as file:
					line = file.readline().strip()
					while line != '':
						blog = json.loads(line, cls=BlogDecoder)
						self.blogs[blog.id] = blog
						line = file.readline().strip()
			except:
				self.blogs ={}
		
	
	def search_blog(self, key):
		return self.blogs.get(key)

	def create_blog(self, blog):
		# add a new blog
		self.blogs[blog.id] = blog
		with open(self.config.blogs_file, 'w') as file:
			for each in self.blogs.values():
				file.write(f"{json.dumps(each, cls=BlogEncoder)}\n")
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
		with open(self.config.blogs_file, 'w') as file:
			for each in self.blogs.values():
				file.write(f"{json.dumps(each, cls=BlogEncoder)}\n")
		return True

	def delete_blog(self, key):
		self.blogs.pop(key)
		with open(self.config.blogs_file, 'w') as file:
			for each in self.blogs.values():
				file.write(f"{json.dumps(each, cls=BlogEncoder)}\n")
		return True

	def list_blogs(self):
		blogs_list = []
		for blog in self.blogs.values():
			blogs_list.append(blog)
		return blogs_list