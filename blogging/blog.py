import datetime
from blogging.post import Post

class Blog():
	''' class that represents a blog '''

	def __init__(self, id, name, url, email):
		''' construct a blog '''
		self.counter = 0
		self.posts = []

		self.id = id
		self.name = name
		self.url = url
		self.email = email

	def __eq__(self, other):
		''' checks whether this blog is the same as other blog '''
		return self.id == other.id and self.name == other.name and self.url == other.url and self.email == other.email

	def __str__(self):
		''' converts the blog object to a string representation '''
		return str(self.id) + "; " + self.name + "; " + self.url + "; " + self.email

	def __repr__(self):
		''' converts the blog object to a string representation for debugging '''
		return "Blog(%r, %r, %r, %r)" % (self.id, self.name, self.url, self.email)

	def search_post(self, code):
		''' search a post in the blog '''
		for post in self.posts:
			if post.code == code:
				return post
		return None

	def create_post(self, title, text):
		''' create a post in the blog '''
		self.counter += 1
		new_post = Post(self.counter, title, text)
		self.posts.append(new_post)
		return new_post

	def retrieve_posts(self, search_string):
		''' retrieve posts in the blog that satisfy a search string '''
		# retrieve existing posts
		retrieved_posts = []
		for post in self.posts:
			if search_string in post.title or search_string in post.text:
				retrieved_posts.append(post)
		return retrieved_posts

	def update_post(self, code, new_title, new_text):
		''' update a post from the blog '''
		updated_post = None

		# first, search the post by code
		for post in self.posts:
			if post.code == code:
				updated_post = post
				break

		# post does not exist
		if not updated_post:
			return False

		# post exists, update fields and update timestamp
		updated_post.update(new_title, new_text)
		return True

	def delete_post(self, code):
		''' delete a post from the blog '''
		post_to_delete_index = -1

		# first, search the post by code
		for i in range(len(self.posts)):
			if self.posts[i].code == code:
				post_to_delete_index = i
				break

		# post does not exist
		if post_to_delete_index == -1:
			return False

		# post exists, delete post
		self.posts.pop(post_to_delete_index)
		return True

	def list_posts(self):
		''' list all posts from the blog from the 
			more recently added to the least recently added'''

		# list existing posts
		posts_list = []
		for i in range(-1, -len(self.posts)-1, -1):
			posts_list.append(self.posts[i])
		return posts_list
