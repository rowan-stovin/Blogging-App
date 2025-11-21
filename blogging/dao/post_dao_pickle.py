import pickle
from blogging.dao.post_dao import PostDAO
from blogging.post import Post
from blogging.configuration import Configuration

# NOTE: The load and save helper methods check if self.autosave internally. I think this cleans up the code and is safer.

class PostDAOPickle(PostDAO):
	def __init__(self, blog_id: int):
		self.posts = []
		self.blog_id = blog_id
		self.autosave = Configuration.autosave 
		
		# We technically don't use this if not autosave
		self.filepath = f'{Configuration.records_path}/{self.blog_id}{Configuration.records_extension}'

		self.load_posts()

	# NOTE: Using RuntimeError for these two helper methods might not be precisely right.
	def load_posts(self) -> None:
		''' a helper method to read from the blog's .dat file to create the self.posts list '''
		if self.autosave:
			try:
				with open(self.filepath, 'rb') as file:
					self.posts = pickle.load(file)
			except FileNotFoundError:
				return None
			except:
				raise RuntimeError('load_posts failed!')
			
	def save_posts(self) -> None:
		''' a helper method to write posts to the blog's .dat file '''
		if self.autosave:
			try:
				with open(self.filepath, 'wb') as file:
					pickle.dump(self.posts, file)
			except:
				raise RuntimeError('save_posts failed!')

	def search_post(self, code) -> Post:
		''' search for a post by code, implicitly returns None if not found '''
		for post in self.posts:
			if post.code == code:
				return post

	def create_post(self, post) -> Post:
		''' create a post in the blog, save if autosave '''
		self.posts.append(post)
		self.save_posts()
		return post

	def retrieve_posts(self, search_string) -> list[Post]:
		''' retrieve posts in the blog that satisfy a search string '''
		return [p for p in self.posts if search_string in p.title or search_string in p.text]

	def update_post(self, code, new_title, new_text) -> bool:
		''' update a post from the blog, save if autosave '''
		updated_post = self.search_post(code)

		# post does not exist
		if not updated_post:
			return False

		# post exists, update fields and update timestamp
		updated_post.update(new_title, new_text)
		self.save_posts()
		return True

	def delete_post(self, code) -> bool:
		''' delete a post from the blog, save if autosave'''
		post_to_delete_index = -1

		# first, search the post by code
		# NOTE: Could probably use search_post somehow. Enumerate, somehow?
		for i in range(len(self.posts)):
			if self.posts[i].code == code:
				post_to_delete_index = i
				break

		# post does not exist
		if post_to_delete_index == -1:
			return False

		# post exists, delete post
		self.posts.pop(post_to_delete_index)
		self.save_posts()
		return True

	def list_posts(self) -> list[Post]:
		''' list all posts from the blog from the 
			more recently added to the least recently added'''
		return self.posts[::-1]