from blogging.post import Post
from blogging.dao.post_dao_pickle import PostDAOPickle

class Blog():
	''' class that represents a blog '''

	def __init__(self, id, name, url, email):
		''' construct a blog '''
		self.id = id
		self.name = name
		self.url = url
		self.email = email

		# NOTE: Assignment PDF says to pass self (blog object) to DAO, but I think this might be better. 
		# Avoids potential circular import. Also, we only need id anyways in DAO (pretty sure, not certain).
		self.post_dao_pickle = PostDAOPickle(self.id)
		
		if self.post_dao_pickle.posts:
			self.counter = self.post_dao_pickle.posts[-1].code
		else:
			self.counter = 0

	def __eq__(self, other):
		''' checks whether this blog is the same as other blog '''
		return self.id == other.id and self.name == other.name and self.url == other.url and self.email == other.email

	def __str__(self):
		''' converts the blog object to a string representation '''
		return str(self.id) + "; " + self.name + "; " + self.url + "; " + self.email

	def __repr__(self):
		''' converts the blog object to a string representation for debugging '''
		return "Blog(%r, %r, %r, %r)" % (self.id, self.name, self.url, self.email)

	def search_post(self, code) -> Post:
		''' search a post in the blog '''
		return self.post_dao_pickle.search_post(code)

	def create_post(self, title, text) -> Post:
		''' create a post in the blog '''
		self.counter += 1
		post = Post(self.counter, title, text)
		return self.post_dao_pickle.create_post(post)

	def retrieve_posts(self, search_string) -> list[Post]:
		''' retrieve posts in the blog that satisfy a search string '''
		return self.post_dao_pickle.retrieve_posts(search_string)

	def update_post(self, code, new_title, new_text) -> bool:
		''' update a post from the blog '''
		return self.post_dao_pickle.update_post(code, new_title, new_text)

	def delete_post(self, code) -> bool:
		''' delete a post from the blog '''
		return self.post_dao_pickle.delete_post(code)

	def list_posts(self) -> list[Post]:
		''' list all posts from the blog from the 
			more recently added to the least recently added'''
		return self.post_dao_pickle.list_posts()
