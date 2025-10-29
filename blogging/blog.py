class Blog:
    def __init__(self, id: int, name: str, url: str, email: str):
        self.id = id
        self.name = name
        self. url = url
        self.email = email

<<<<<<< HEAD
=======
    def __eq__(self, other) -> bool:
        return self.id == other.id \
            and self.name == other.name \
            and self.url == other.url \
            and self.email == other.email
>>>>>>> ad656915932e1ee0e6ebdb05d2ce51252fcb862a
