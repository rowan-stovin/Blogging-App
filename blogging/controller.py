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

    def set_current_blog(self, cur_id: int):
        
        #should something be returned?
        self.current_blog = self.search_blog(cur_id)

    #unsets current blog
    def unset_current_blog(self):
        self.current_blog = None

    #gets current blog
    def get_current_blog(self):
        if self.logged_in:
            return self.current_blog

        #maybe return False
        return None

    #creates new blog
    def create_blog(self, id: int, name: str, url: str, email: str) -> Blog:
        # If user isn't logged in, or blog already exists
        if not self.logged_in or self.blog_collection.get(id):
            return

        self.blog_collection[id] = Blog(id, name, url, email)
        return self.blog_collection[id]


    def update_blog(self, old_id: int, new_id: int, name: str, url: str, email: str) -> bool:
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
            del self.blog_collection[old_id]

        return True

    #deletes blog with given id
    def delete_blog(self, id: int) -> bool:
        blog = self.search_blog(id)

        if not self.logged_in:
            return False
        elif blog == None:
            return False
        elif blog == self.current_blog:
            return False

        del self.blog_collection[id]
        return True

    #searches blog by id
    def search_blog(self, id: int) -> Blog:
        return self.blog_collection.get(id)

    #retrieves a list of blogs with keyword in its name
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
        # We could probably make this into a helper method if we wanted to.
        if not self.logged_in or not self.current_blog:
            return

        # NOTE: There is probably a cleaner way to do this.
        # The post number ("code") is the 1-th index for the blog's posts.
        # We could probably change this field name in post.py, would be more readable.

        code = len(self.current_blog.post_collection) + 1
        post = Post(code, title, text)
        self.current_blog.post_collection[code] = post

        return post

    def update_post(self, code: int, title: str, text: str):
        if not self.logged_in or not self.current_blog:
            return False
        
        # No current Blog
        if self.current_blog == None:
            return False
        
        # No posts to update
        if self.current_blog.post_collection == {}:
            return False
        
        self.current_blog.post_collection[code] = self.create_post(title, text)
        return True
    
    def search_post(self, code: int) -> Post:
        if not self.logged_in or not self.current_blog:
            return

        return self.current_blog.post_collection.get(code)


    def delete_post(self, code: int):
        """A method to delete a post in the current blog with a given code. Does not shift post code..."""
        if not self.logged_in or not self.current_blog:
            return False
        
        if not self.current_blog.post_collection.get(code):
            return False

        # NOTE: Do we need to shift post code's if we delete a post?
        # I don't think we do, because this method passes tests.
        del self.current_blog.post_collection[code]
        return True


    def list_posts(self) -> list[Post]:
        """A method that returns the current blog's post collection (as a list)."""
        if not self.logged_in or not self.current_blog:
            return

        # A list of the posts, reversed with string slicing.
        return list(self.current_blog.post_collection.values())[::-1]


    def retrieve_posts(self, keyword: str) -> list[Post]:
        """A method to return all posts in the current blog that have keyword in the title or text."""
        if not self.logged_in or not self.current_blog:
            return
        
        return [p for p in self.current_blog.post_collection.values() if keyword in p.title or keyword in p.text]
