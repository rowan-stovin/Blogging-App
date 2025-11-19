from blogging.blog import Blog
from blogging.post import Post
from blogging.exception.duplicate_login_exception import DuplicateLoginException
from blogging.exception.illegal_access_exception import IllegalAccessException
from blogging.exception.illegal_operation_exception import IllegalOperationException
from blogging.exception.invalid_login_exception import InvalidLoginException
from blogging.exception.invalid_logout_exception import InvalidLogoutException
from blogging.exception.no_current_blog_exception import NoCurrentBlogException


class Controller():
	''' controller class that receives the system's operations '''

	def __init__(self):
		''' construct a controller class '''
		self.users = {"user" : "blogging2025"}

		self.username = None
		self.password = None
		self.logged = False

		self.blogs = {}
		self.current_blog = None

	def login(self, username, password):
		''' user logs in the system '''
		if self.logged:
			raise IllegalAccessException
		if username in self.users:
			if password == self.users[username]:
				self.username = username
				self.password = password
				self.logged = True
				return True
			else:
				raise IllegalAccessException
		else:
			raise IllegalAccessException

	def logout(self):
		''' user logs out from the system '''
		if not self.logged:
			raise IllegalAccessException
		else:
			self.username = None
			self.password = None
			self.logged = False
			self.current_blog = None
			return True

	def search_blog(self, id):
		''' user searches a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		return self.blogs.get(id)

	def create_blog(self, id, name, url, email):
		''' user creates a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# blog already exists, do not create them
		if self.blogs.get(id):
			return None

		# finally, create a new blog
		blog = Blog(id, name, url, email)
		self.blogs[id] = blog
		return blog

	def retrieve_blogs(self, name):
		''' user retrieves the blogs that satisfy a search criterion '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		retrieved_blogs = []
		for blog in self.blogs.values():
			if name in blog.name:
				retrieved_blogs.append(blog)
		return retrieved_blogs

	def update_blog(self, original_id, id, name, url, email):
		''' user updates a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blogs.get(original_id)

		# blog does not exist, cannot update
		if not blog:
			return False

		# blog is current blog, cannot update
		if self.current_blog:
			if blog == self.current_blog:
				return False

		# blog exists, update fields
		blog.name = name
		blog.url = url
		blog.email = email

		# treat different keys as a separate case
		if original_id != id:
			if self.blogs.get(id):
				return False
			self.blogs.pop(original_id)
			blog.id = id
			self.blogs[id] = blog

		return True
			
	def delete_blog(self, id):
		''' user deletes a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blogs.get(id)

		# blog does not exist, cannot delete
		if not blog:
			return False

		# blog is current blog, cannot delete
		if self.current_blog:
			if blog == self.current_blog:
				return False

		# blog exists, delete blog
		self.blogs.pop(id)
		return True

	def list_blogs(self):
		''' user lists all blogs '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		blogs_list = []
		for blog in self.blogs.values():
			blogs_list.append(blog)
		return blogs_list

	def set_current_blog(self, id):
		''' user sets the current blog '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blogs.get(id)

		# blog does not exist
		if not blog:
			return False

		# blog exists, set them to be the current blog
		self.current_blog = blog


	def get_current_blog(self):
		''' get the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# return current blog
		return self.current_blog

	def unset_current_blog(self):
		''' unset the current blog '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# unset current blog
		self.current_blog = None


	def search_post(self, code):
		''' user searches a post from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		# search a new post with the given code and return it 
		return self.current_blog.search_post(code)

	def create_post(self, title, text):
		''' user creates a post in the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		# create a new post and return it
		return self.current_blog.create_post(title, text)

	def retrieve_posts(self, search_string):
		''' user retrieves the posts from the current blog
			that satisfy a search string '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		# return the found posts
		return self.current_blog.retrieve_posts(search_string)

	def update_post(self, code, new_title, new_text):
		''' user updates a post from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		# update post
		return self.current_blog.update_post(code, new_title, new_text)

	def delete_post(self, code):
		''' user deletes a post from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		# delete post
		return self.current_blog.delete_post(code)

	def list_posts(self):
		''' user lists all posts from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			return None

		return self.current_blog.list_posts()
