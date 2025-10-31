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
        self.username = username


    def set_password(self, password: int) -> None:
        self.password = password


    def login(self, username: str, password: str) -> bool:
        # Can't login if already logged in
        if self.logged_in:
            return False
        elif self.username != username or self.password != password:
            return False

        self.logged_in = True
        return True


    def logout(self) -> bool:
        if not self.logged_in:
            return False

        self.set_password = None
        self.set_username = None
        self.logged_in = False

        return True


    # Blog methods

    def set_current_blog(self, new_id: int):
        raise NotImplementedError


    def get_current_blog(self):
        raise NotImplementedError


    def create_blog(self, id: int, name: str, url: str, email: str) -> Blog:
        # If user isn't logged in, or blog already exists
        if not self.logged_in or self.blog_collection.get(id):
            return

        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]


    def update_blog(self, old_id: int, new_id: int, name: str, url: str, email: str) -> bool:
        if not self.logged_in or not self.blog_collection:
            return False

        # We don't want to update to an existing id, unless we are modifying a blog and keeping same id.
        if self.blog_collection.get(new_id) and old_id != new_id:
            return False

        # We update values even if id is the same
        self.blog_collection[new_id] = Blog(new_id, name, url, email)

        # Delete old (if exists) if not same as new (because it hasn't been overridden)
        if self.blog_collection.get(old_id) and old_id != new_id:
            del self.blog_collection[old_id]

        return True


    def delete_blog(self, id: int) -> bool:
        raise NotImplementedError

    def search_blog(self, id: int) -> Blog:
        return self.blog_collection.get(id)

    def retrieve_blogs(self, keyword) -> list[Blog]:
        if not self.logged_in:
            return

        blogs = []
        for blog in self.blog_collection.values():
            if keyword in blog.name:
                blogs.append(blog)

        return blogs


    def list_blogs(self) -> list[Blog]:
        if not self.logged_in:
            return

        return [blog for blog in self.blog_collection.values()]


    # Post methods

    def create_post(self, title: str, text: str) -> Post:
        raise NotImplementedError


    def update_post(self, code:int, title: str, text: str):
        raise NotImplementedError


    def delete_post(self, code: int):
        raise NotImplementedError


    def list_posts(self):
        raise NotImplementedError


    def retrieve_posts(self, blog: Blog):
        raise NotImplementedError
