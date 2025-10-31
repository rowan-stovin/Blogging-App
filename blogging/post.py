from datetime import datetime

class Post:
    def __init__(self, code: int, title: str, text: str):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.now()
        self.update = None
