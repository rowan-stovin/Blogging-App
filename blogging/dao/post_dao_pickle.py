import pickle
from blogging.dao.post_dao import PostDAO
from blogging.post import Post

class PostDAOPickle(PostDAO):
	def __init__(self, blog):
		self.posts = []

		# TODO: Add code for loading posts from blog
		# I think this is 3.3 in the PDF?

		# This import is in the __init__ method to avoid circular imports. There might be a better solution.
		from blogging.blog import Blog
		self.blog = blog # we pass "self" in blog.py, which is the Blog object itself here, as self.blog

	def search_post(self, code) -> Post:
		for post in self.posts:
			if post.code == code:
				return post

	def create_post(self, post) -> Post:
		''' create a post in the blog '''
		self.posts.append(post)
		return post

	def retrieve_posts(self, search_string) -> list[Post]:
		''' retrieve posts in the blog that satisfy a search string '''
		return [p for p in self.posts if search_string in p.title or search_string in p.text]

	def update_post(self, code, new_title, new_text) -> bool:
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

	def delete_post(self, code) -> bool:
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
		# NOTE: I think we should reserialize/resave here, but I am not sure.
		return True

	def list_posts(self) -> list[Post]:
		''' list all posts from the blog from the 
			more recently added to the least recently added'''

		# list existing posts
		posts_list = []
		for i in range(-1, -len(self.posts)-1, -1):
			posts_list.append(self.posts[i])
		return posts_list