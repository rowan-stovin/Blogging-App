from blogging.post import Post

class Blog:
    def __init__(self, id: int, name: str, url: str, email: str):
        self.id = id
        self.name = name
        self. url = url
        self.email = email
        self.post_collection = {}

    """Compares two blogs"""
    def __eq__(self, other) -> bool:
        # I don't like this for some reason but I guess it works.
        if not other: return False

        return self.id == other.id \
            and self.name == other.name \
            and self.url == other.url \
            and self.email == other.email

    """Creates a post"""
    def create_post(self, title: str, text: str) -> Post:
        # NOTE: There is probably a cleaner way to do this.
        # The post number ("code") is the 1-th index for the blog's posts.
        # When we list_posts, we return this reversed (highest code first, like a feed).
        # We could probably change this field name in post.py, would be more readable.

        code = len(self.post_collection) + 1
        post = Post(code, title, text)
        self.post_collection[code] = post

        return post

    """Updates the post at the given code"""
    def update_post(self, code: int, title: str, text: str):
        self.post_collection[code] = Post(code, title, text)
        return True

    """Searches for a post in the current Blogs collection"""
    def search_post(self, code: int) -> Post:
        return self.post_collection.get(code)

    """Deletes a post in the current blog with the given code. Does not shift post code..."""
    def delete_post(self, code: int):
        if self.post_collection == {}:
            return False
        
        # NOTE: We don't need to shift post codes, IDK why.
        del self.post_collection[code]
        return True

    """Lists the Blog's post collection"""
    def list_posts(self) -> list[Post]:
        # A list of the posts, reversed with slicing (like a feed).
        return list(self.post_collection.values())[::-1]

    """Lists all posts in the Blog that have the given keyword in the title or text."""
    def retrieve_posts(self, keyword: str) -> list[Post]:
        # For value (post) in posts if keword in that post title or text.
        return [p for p in self.post_collection.values() if keyword in p.title or keyword in p.text]

