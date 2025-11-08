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
        # (from what it says in test file).
        # Also, time's aren't even used in this assignment, pretty sure.
        # Guess for next assignment!
        return self.code == other.code \
            and self.title == other.title \
            and self.text == other.text

    def __repr__(self) -> str:
        """String representation of a Blog"""
        
        return f"Blog(code: {self.code}, title: {self.title}, url: {self.text}, creation date: {self.creation}, update date: {self.update})"
    