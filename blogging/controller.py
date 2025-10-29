from blog import Blog
from post import Post

class Controller:
    def __init__(self):
        self.login_flag = False
        self.username = ""
        self.password = ""
    
    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: int):
        self.password = password

    def logout(self):
        return self.login_flag
    
    def login(self, username, password):
        if(self.login_flag):
            return "cannot login again while still logged in"
        elif(not username.equals(self.username)):
            return "login in with incorrect username"
        elif(not password.equals(self.password)):
            return "login in with incorrect password"
        
        
