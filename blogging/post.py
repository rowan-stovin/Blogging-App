from datetime import datetime

class Post:
    def __init__(self, code: int, title: str, text: str, creation: DateTime, update: DateTime):
        self.code = code
        self.title = title
        self.text = text
        self.creation = creation
        self.update = update
