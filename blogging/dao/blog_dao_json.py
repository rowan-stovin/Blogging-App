import json
from blogging.blog import Blog
from blogging.dao.blog_dao import BlogDAO
from blogging.dao.blog_encoder import BlogEncoder
from blogging.dao.blog_decoder import BlogDecoder
from blogging.configuration import Configuration


class BlogDAOJSON(BlogDAO):
	def __init__(self):
		self.blogs = {}
		self.autosave = Configuration.autosave
		self.filepath = Configuration.blogs_file
		self.load_blogs()
	
	def load_blogs(self) -> None:
		''' a helper method to load blogs '''
		if self.autosave:
			try:
				with open(self.filepath, 'r') as file:
					line = file.readline().strip()

					while line:
						blog = json.loads(line, cls=BlogDecoder)
						self.blogs[blog.id] = blog
						line = file.readline().strip()

			except FileNotFoundError:
				return None
			except:
				raise RuntimeError("load_blogs failed!")
	
	def save_blogs(self) -> None:
		''' a helper method to save blogs '''
		if self.autosave:
			with open(self.filepath, 'w') as file:
				for blog in self.blogs.values():
					file.write(f"{json.dumps(blog, cls=BlogEncoder)}\n")

	def search_blog(self, key) -> Blog:
		''''''
		return self.blogs.get(key)

	def create_blog(self, blog) -> Blog:
		''''''
		# add a new blog
		self.blogs[blog.id] = blog
		self.save_blogs()
		return blog

	def retrieve_blogs(self, search_string) -> list[Blog]:
		''''''
		return [b for b in self.blogs.values() if search_string in b.name]

	def update_blog(self, key, blog) -> bool:
		''''''
		self.blogs.pop(blog.id)
		blog.id = key
		self.blogs[key] = blog
		self.save_blogs()
		return True

	def delete_blog(self, key) -> bool:
		''''''
		self.blogs.pop(key)
		self.save_blogs()
		return True

	def list_blogs(self) -> list[Blog]:
		''''''
		return [b for b in self.blogs.values()]