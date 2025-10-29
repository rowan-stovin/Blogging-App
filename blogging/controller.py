from blog import Blog
from post import Post

class Controller:
    def __init__(self):
        self.logged_in = False
        self.username = None
        self.password = None
        self.blog_collection = {}
    
    def set_username(self, username: str) -> None:
        self.username = username

    def set_password(self, password: int) -> None:
        self.password = password

    def logout(self) -> bool:
        if not self.logged_in:
            return False

        self.set_password = None
        self.set_username = None
        self.logged_in = False

        return True

    def login(self, username: str, password: str) -> bool:
        # Can't login if already logged in
        if self.logged_in:
            return False
        elif self.username != username or self.password != password:
            return False

        self.logged_in = True
        return True

    def create_blog(self, id: int, name: str, url: str, email: str) -> Blog:
        # If user isn't logged in, or blog already exists
        if not self.logged_in or self.blog_collection[id]:
            return None

        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]

    def search_blog(self, id: int) -> Blog:
        return self.blog_collection[id]

    def update_blog(self, old_id: int, new_id: int, name: str, url: str, email: str):
        if old_id == new_id:
            return self.blog_collection[old_id]

        self.blog_collection[new_id] = self.create_blog(new_id, name, url, email)
        self.blog_collection[old_id] = None

        return self.blog_collection[new_id]

    def retrieve_blogs(self, name):
        blogs = []
        if(not self.logged_in):
            return
        for each in self.blog_collection:
            if name is each.self.name:
                blogs.append(each)

        return blogs