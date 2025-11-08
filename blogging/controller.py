from blogging.blog import Blog
from blogging.post import Post

class Controller:
    def __init__(self):
        self.logged_in = False
        self.username = "user"
        self.password = "blogging2025"
        self.blog_collection = {}
        self.current_blog = None

    def set_username(self, username: str) -> None:
        """Sets their username"""
        self.username = username

    def set_password(self, password: int) -> None:
        """Sets their password"""
        self.password = password

    def login(self, username: str, password: str) -> bool:
        """Logs in the user if not already logged in and username/password is correct"""
        if self.logged_in:
            return False
        elif self.username != username or self.password != password:
            return False

        self.logged_in = True
        return True

    def logout(self) -> bool:
        """Logs out the user"""
        if not self.logged_in:
            return False

        self.set_password = None
        self.set_username = None
        self.logged_in = False

        return True


    # --- Blog methods ---

    def set_current_blog(self, cur_id: int):
        """Set current blog"""
        self.current_blog = self.search_blog(cur_id)

    def unset_current_blog(self):
        """Unsets current blog"""
        self.current_blog = None

    def get_current_blog(self):
        """Gets current blog"""
        if self.logged_in:
            return self.current_blog


    def create_blog(self, id: int, name: str, url: str, email: str) -> Blog:
        """Creates new blog"""
        # If user isn't logged in, or blog already exists
        if not self.logged_in or self.blog_collection.get(id):
            return

        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]

    def update_blog(self, old_id: int, new_id: int, name: str, url: str, email: str) -> bool:
        """Updates the blog, can change its id"""
        if not self.logged_in or not self.blog_collection:
            return False

        # Cannot update current blog (if there is a current blog)
        if self.current_blog == self.blog_collection.get(new_id) and self.current_blog:
            return False

        # We don't want to update to an existing id, unless we are modifying a blog and keeping same id.
        if self.blog_collection.get(new_id) and old_id != new_id:
            return False

        # We update values even if id is the same
        self.blog_collection[new_id] = Blog(new_id, name, url, email)

        # Delete old (if exists) if not same as new (because it hasn't been overridden)
        if self.blog_collection.get(old_id) and old_id != new_id:
            self.delete_blog(old_id)

        return True

    def delete_blog(self, id: int) -> bool:
        """Deletes blog with the given id."""
        blog = self.search_blog(id)

        if not self.logged_in or not blog:
            return False

        # Can't delete current blog
        if blog == self.get_current_blog():
            return False

        del self.blog_collection[id]
        return True

    def search_blog(self, id: int) -> Blog:
        """Searches for blog with given id."""
        return self.blog_collection.get(id)

    def list_blogs(self) -> list[Blog]:
        """Returns a list of all blogs"""
        if not self.logged_in:
            return

        return [blog for blog in self.blog_collection.values()]

    def retrieve_blogs(self, keyword) -> list[Blog]:
        """Retrieves a list of blogs with keyword in name."""
        if not self.logged_in:
            return

        return [blog for blog in self.blog_collection.values() if keyword in blog.name]


    # --- Post methods ---

    def create_post(self, title: str, text: str) -> Post:
        """Create a post, if logged in and current blog."""
        if not self.logged_in or not self.current_blog:
            return

        return self.get_current_blog().create_post(title, text)

    def update_post(self, code: int, title: str, text: str):
        # If logged in and theres a valid current blog then updates the post, otherwise returns None
        if not self.logged_in or not self.current_blog:
            return False

        # No posts to update
        if not self.get_current_blog().search_post(code):
            return False

        self.get_current_blog().update_post(code, title, text)
        return True

    """If logged in and there's a valid current blog then searches for a post, otherwise returns None"""
    def search_post(self, code: int) -> Post:
        if not self.logged_in:
            return

        return self.get_current_blog().search_post(code)

    """If logged in and there's a valid current blog then deletes blog with given code"""
    def delete_post(self, code: int):
        if not self.logged_in or not self.current_blog:
            return False

        # NOTE: We don't need to shift post codes, IDK why.
        return self.current_blog.delete_post(code)

    """If logged in Lists the valid current Blogs post, otherwise returns None"""
    def list_posts(self) -> list[Post]:
        if not self.logged_in or not self.current_blog:
            return

        return self.current_blog.list_posts()

    """If logged in Retrieves the valid current Blog's posts, otherwise returns None"""
    def retrieve_posts(self, keyword: str) -> list[Post]:
        if not self.logged_in or not self.current_blog:
            return

        # For value (post) in posts if keword in that post title or text.
        return self.current_blog.retrieve_posts(keyword)
