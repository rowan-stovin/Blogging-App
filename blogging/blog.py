class Blog:
    def __init__(self, id: int, name: str, url: str, email: str):
        self.id = id
        self.name = name
        self. url = url
        self.email = email
        self.post_collection = {}

    def __eq__(self, other) -> bool:
        # I don't like this for some reason but I guess it works.
        if not other: return False

        return self.id == other.id \
            and self.name == other.name \
            and self.url == other.url \
            and self.email == other.email
