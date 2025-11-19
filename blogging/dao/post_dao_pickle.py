from blogging.dao.post_dao import PostDAO

class PostDAOPPickle(PostDAO):
    def __init__(self):
        # post collection here, I am pretty sure.
        pass
    
    def search_post(self, key):
        pass

    def create_post(self, post):
        pass

    def retrieve_posts(self, search_string):
        pass

    def update_post(self, key, new_title, new_text):
        pass

    def delete_post(self, key):
        pass

    def list_posts(self):
        pass
