from datetime import datetime

class Post:
    def __init__(self, code: int, title: str, text: str):
        self.code = code
        self.title = title
        self.text = text
        self.creation = datetime.now()
        self.update = None

    def __eq__(self, other):
        # I don't think we need to compare datatime's
        # From what it says in test file.
        return self.code == other.code \
            and self.title == other.title \
            and self.text == other.text
