from blogging.blog import Blog
from blogging.post import Post

class Controller:
    def __init__(self):
        self.logged_in = False
        self.username = "user"
        self.password = "blogging2025"
        self.blog_collection = {}
        self.current_blog = None

    """Sets their username"""
    def set_username(self, username: str) -> None:
        self.username = username

    """Sets their password"""
    def set_password(self, password: int) -> None:
        self.password = password

    """logs in the user if not already logged in and username/password is correct"""
    def login(self, username: str, password: str) -> bool:
        if self.is_logged_in():
            return False
        elif self.username != username or self.password != password:
            return False

        self.logged_in = True
        return True

    """Logs out the user"""
    def logout(self) -> bool:
        if not self.is_logged_in():
            return False

        self.set_password = None
        self.set_username = None
        self.logged_in = False

        return True
    
    """Checks if they are logged in"""
    def is_logged_in(self):
        if self.logged_in:
            return True
        
        return False
    
    """Checks if theres a current blog"""
    def valid_current_blog(self):
        if not self.current_blog:
            return False
        
        return True
    
    # --- Blog methods ---

    """Set current blog"""
    def set_current_blog(self, cur_id: int):
        self.current_blog = self.search_blog(cur_id)

    """unsets current blog"""
    def unset_current_blog(self):
        self.current_blog = None

    """gets current blog"""
    def get_current_blog(self):
        if self.logged_in:
            return self.current_blog

        return None


    """creates new blog"""
    def create_blog(self, id: int, name: str, url: str, email: str) -> Blog:
        # If user isn't logged in, or blog already exists
        if not self.is_logged_in() or self.blog_collection.get(id):
            return None

        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]

    """Updates the blog, can change its id"""
    def update_blog(self, old_id: int, new_id: int, name: str, url: str, email: str) -> bool:
        if not self.is_logged_in() or not self.blog_collection:
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

    """Deletes blog with the given id."""
    def delete_blog(self, id: int) -> bool:
        blog = self.search_blog(id)
        
        if not self.is_logged_in():
            return False
        elif not blog:
            return False
        elif blog == self.get_current_blog():
            return False
        
        del self.blog_collection[id]
        return True

    """Searches for blog with given id."""
    def search_blog(self, id: int) -> Blog:
        return self.blog_collection.get(id)

    """Lists the blogs"""
    def list_blogs(self) -> list[Blog]:
        if not self.is_logged_in():
            return None

        return [blog for blog in self.blog_collection.values()]

    """Retrieves a list of blogs with keyword in name."""
    def retrieve_blogs(self, keyword) -> list[Blog]:
        if not self.is_logged_in():
            return None
        
        # TODO: Refactor to list comprehension.
        blogs = []
        for blog in self.blog_collection.values():
            if keyword in blog.name:
                blogs.append(blog)

        return blogs


    # --- Post methods ---

    """If logged in and theres a valid current blog then creates post, otherwise returns None"""
    def create_post(self, title: str, text: str) -> Post:
        if not self.is_logged_in() or not self.valid_current_blog():
            return None
        
        return self.get_current_blog().create_post(title, text)
    
    """If logged in and theres a valid current blog then updates the post, otherwise returns None"""
    def update_post(self, code: int, title: str, text: str):
        if not self.is_logged_in() or not self.valid_current_blog():
            return False

        # No posts to update
        if not self.get_current_blog().search_post(code):
            return False

        self.get_current_blog().update_post(code, title, text)
        return True
    
    """If logged in and there's a valid current blog then searches for a post, otherwise returns None"""
    def search_post(self, code: int) -> Post:
        if not self.is_logged_in():
            return None

        return self.get_current_blog().search_post(code)
    
    """If logged in and there's a valid current blog then deletes blog with given code"""
    def delete_post(self, code: int):
        if not self.is_logged_in() or not self.valid_current_blog():
            return False

        # NOTE: We don't need to shift post codes, IDK why.
        return self.current_blog.delete_post(code)
        
    """If logged in Lists the valid current Blogs post, otherwise returns None"""
    def list_posts(self) -> list[Post]:
        if not self.is_logged_in() or not self.valid_current_blog():
            return None

        # A list of the posts, reversed with slicing (like a feed).
        return self.current_blog.list_posts()
    
    """If logged in Retrieves the valid current Blog's posts, otherwise returns None"""
    def retrieve_posts(self, keyword: str) -> list[Post]:
        if not self.is_logged_in() or not self.valid_current_blog():
            return None

        # For value (post) in posts if keword in that post title or text.
        return self.current_blog.retrieve_posts(keyword)
    