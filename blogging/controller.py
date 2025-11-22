import hashlib
from blogging.blog import Blog
from blogging.post import Post
from blogging.configuration import Configuration
from blogging.dao.blog_dao_json import BlogDAOJSON
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
		self.autosave = Configuration.autosave
		self.users = {}
		self.username = None
		self.password = None
		self.logged = False
		
		self.blog_dao_json = BlogDAOJSON()
		self.current_blog = None

		# NOTE: We omit a conditional check of if self.autosave here,
		# and we always load from users.txt
		# In the class disscussion forum, a student asked about this,
		# and Professor Bittencourt said that this is fine,
		# as the assignment specfiication was "a bit dubious".
		# See the post with title: "Persistence vs unittest" in the A4 thread.

		try:
			with open(Configuration.users_file, "r") as file:
				for line in file:
					line = line.strip()

					if not line: 
						continue

					parts = line.split(",")
					username, password = parts
					self.users[username] = password

		except FileNotFoundError:
			raise FileNotFoundError("users.txt was not found!")
		except Exception as e:
			raise RuntimeError(f"Error loading users: {e}")
	

	def get_password_hash(self, password):
		encoded_password = password.encode('utf-8')     # Convert the password to bytes
		hash_object = hashlib.sha256(encoded_password)      # Choose a hashing algorithm (e.g., SHA-256)
		hex_dig = hash_object.hexdigest()       # Get the hexadecimal digest of the hashed password
		return hex_dig

	def login(self, username, password):
		''' user logs in the system '''
		if self.logged:
			raise DuplicateLoginException
		if username in self.users:
			if self.get_password_hash(password) == self.users[username]:
				self.username = username
				self.password = self.get_password_hash(password)
				self.logged = True
				return True
			else:
				raise InvalidLoginException
		else:
			raise InvalidLoginException

	def logout(self):
		''' user logs out from the system '''
		if not self.logged:
			raise InvalidLogoutException
		
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

		return self.blog_dao_json.search_blog(id)

	def create_blog(self, id, name, url, email):
		''' user creates a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# blog already exists, do not create them
		if self.blog_dao_json.search_blog(id):
			raise IllegalOperationException

		# finally, create a new blog
		blog = Blog(id, name, url, email)
		return self.blog_dao_json.create_blog(blog)

	def retrieve_blogs(self, name):
		''' user retrieves the blogs that satisfy a search criterion '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		return self.blog_dao_json.retrieve_blogs(name)

	def update_blog(self, original_id, id, name, url, email):
		''' user updates a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blog_dao_json.search_blog(original_id)

		# blog does not exist, cannot update
		if not blog:
			raise IllegalOperationException

		# blog is current blog, cannot update
		if self.current_blog:
			if blog == self.current_blog:
				raise IllegalOperationException

		# blog exists, update fields
		blog.name = name
		blog.url = url
		blog.email = email

		# treat different keys as a separate case
		if original_id != id:
			if self.blog_dao_json.search_blog(id):
				raise IllegalOperationException

		return self.blog_dao_json.update_blog(id, blog)
			
	def delete_blog(self, id):
		''' user deletes a blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blog_dao_json.search_blog(id)

		# blog does not exist, cannot delete
		if not blog:
			raise IllegalOperationException

		# blog is current blog, cannot delete
		if self.current_blog:
			if blog == self.current_blog:
				raise IllegalOperationException

		# blog exists, delete blog
		return self.blog_dao_json.delete_blog(id)

	def list_blogs(self):
		''' user lists all blogs '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		return self.blog_dao_json.list_blogs()

	def set_current_blog(self, id):
		''' user sets the current blog '''

		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# first, search the blog by key
		blog = self.blog_dao_json.search_blog(id)

		# blog does not exist
		if not blog:
			raise IllegalOperationException

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
			raise NoCurrentBlogException

		# search a new post with the given code and return it 
		return self.current_blog.search_post(code)

	def create_post(self, title, text):
		''' user creates a post in the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			raise NoCurrentBlogException

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
			raise NoCurrentBlogException

		# return the found posts
		return self.current_blog.retrieve_posts(search_string)

	def update_post(self, code, new_title, new_text):
		''' user updates a post from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			raise NoCurrentBlogException

		# update post
		return self.current_blog.update_post(code, new_title, new_text)

	def delete_post(self, code):
		''' user deletes a post from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			raise NoCurrentBlogException

		# delete post
		return self.current_blog.delete_post(code)

	def list_posts(self):
		''' user lists all posts from the current blog '''
		# must be logged in to do operation
		if not self.logged:
			raise IllegalAccessException

		# there must be a valid current blog
		if not self.current_blog:
			raise NoCurrentBlogException

		return self.current_blog.list_posts()
