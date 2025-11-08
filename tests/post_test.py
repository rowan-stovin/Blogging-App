from unittest import TestCase
from unittest import main
from blogging.post import Post

class PostTest(TestCase):
    
    def test_post_equality(self):
        return
    
    def test_post_repr(self):
        p1 = Post(1, "First Post", "This is my first post. It's so easy!")
        p2 = Post(2, "Latest Post", "Wow, these guys deserve an A++")
        result_1 = repr(p1)
        result_2 = repr(p2)

        self.assertIn("1", result_1)
        self.assertIn("First Post", result_1)
        self.assertIn("This is my first post. It's so easy!", result_1)

        self.assertIn("2", result_2)
        self.assertIn("Latest Post", result_2)
        self.assertIn("Wow, these guys deserve an A++", result_2)

if __name__ == '__main__':
	unittest.main()