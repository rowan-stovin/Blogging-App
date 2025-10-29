from blog import Blog
from post import Post

class Controller:
    def __init__(self):
        self.login_flag = False
        self.username = None
        self.password = None
    
    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: int):
        self.password = password

    def logout(self):
        if not self.login_flag:
            return False
        
        self.set_password = None
        self.set_username = None

        return True
    
    def login(self, username: str, password: str):
        if self.login_flag:
            return False
        elif not username == self.username:
            return False
        elif not password == self.password:
            return False
        else:
            return True
        
    def create_blog(self, id: int, name: str, url: str, email: str):
        if not self.login_flag:
            return None
        
        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]

    def search_blog(self, id: int):
        return self.blog_collection[id]
        

