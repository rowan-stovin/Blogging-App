from unittest import TestCase
from unittest import main
from blogging.blog import Blog
from blogging.post import Post

class BlogTest(TestCase):

    def test_blog_equality(self):
        b1 = Blog(1111114444, "Short Journey", "short_journey", "short.journey@gmail.com")
        b1a = Blog(1111114444, "Short Journey", "short_journey", "short.journey@gmail.com")
        b2 = Blog(1111115555, "Long Journey", "long_journey", "long.journey@gmail.com")

        self.assertFalse(b1 == b2)
        self.assertTrue(b1 == b1)
        self.assertTrue(b1 == b1a)
    
    def test_blog_repr(self):
        b1 = Blog(1111114444, "Short Journey", "short_journey", "short.journey@gmail.com")
        b2 = Blog(1111115555, "Long Journey", "long_journey", "long.journey@gmail.com")
        result_1 = repr(b1)
        result_2 = repr(b2)

        self.assertIn("1111114444", result_1)
        self.assertIn("Short Journey", result_1)
        self.assertIn("short_journey", result_1)
        self.assertIn("short.journey@gmail.com", result_1)

        self.assertIn("1111115555", result_2)
        self.assertIn("Long Journey", result_2)
        self.assertIn("long_journey", result_2)
        self.assertIn("long.journey@gmail.com", result_2)

    def test_create_post(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")
        expected_post = Post(1, "First Post", "This is my first post. It's so easy!")

        self.assertEqual(blog.create_post("First Post", "This is my first post. It's so easy!"), expected_post)

        expected_post = Post(2, "Latest Post", "Wow, these guys deserve an A++")
        self.assertEqual(blog.create_post("Latest Post", "Wow, these guys deserve an A++"), expected_post)

    def test_update_post(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")

        blog.create_post("First Post", "This is my first post. It's so easy!")
        blog.create_post("Latest Post", "Wow, these guys deserve an A++")

        self.assertTrue(blog.update_post(1, "My First Post", "This is my first post. It's so hard!"))
        expected_p1 = Post(1, "My First Post", "This is my first post. It's so hard!")
        actual_p1 = blog.search_post(1)
        self.assertEqual(expected_p1, actual_p1)

        self.assertTrue(blog.update_post(2, "My Latest Post", "Amazing! These guys deserve an A++"))
        expected_p2 = Post(2, "My Latest Post", "Amazing! These guys deserve an A++")
        actual_p2 = blog.search_post(2)
        self.assertEqual(expected_p2, actual_p2)

    def test_search_post(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")
        
        blog.create_post("First Post", "This is my first post. It's so easy!")
        blog.create_post("Latest Post", "Wow, these guys deserve an A++")

        self.assertIsNotNone(blog.search_post(1))
        self.assertIsNotNone(blog.search_post(2))
        self.assertIsNone(blog.search_post(3))

        expected_post = Post(1, "First Post", "This is my first post. It's so easy!")
        self.assertEqual(blog.search_post(1), expected_post)

        expected_post = Post(2, "Latest Post", "Wow, these guys deserve an A++")
        self.assertEqual(blog.search_post(2), expected_post)
    
    def test_delete_post(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")

        blog.create_post("First Post", "This is my first post. It's so easy!")
        blog.create_post("Latest Post", "Wow, these guys deserve an A++")

        self.assertTrue(blog.delete_post(1))
        self.assertTrue(blog.delete_post(2))
    
    def test_list_posts(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")

        expected_list = [Post(3, "Latest Post", "Wow, these devs are so intelligent!"),
                         Post(2, "New Post", "Wow, these guys deserve an A++"),
                         Post(1, "First Post", "Wow, This is my first post. It's so easy!")
                         ]

        self.assertNotEqual(blog.list_posts(), expected_list)
        self.assertEqual(blog.list_posts(), [])

        blog.create_post("First Post", "Wow, This is my first post. It's so easy!")
        blog.create_post("New Post", "Wow, these guys deserve an A++")
        blog.create_post("Latest Post", "Wow, these devs are so intelligent!")

        self.assertEqual(blog.list_posts(), expected_list)

    def test_retrieve_posts(self):
        blog = Blog(1111114444, "First Journey", "first_journey", "first.journey@gmail.com")

        blog.create_post("First Post", "Wow, This is my first post. It's so easy!")
        blog.create_post("New Post", "Wow, these guys deserve an A++")
        blog.create_post("Latest Post", "Wow, these devs are so intelligent!")

        expected_post_1 = Post(1, "First Post", "Wow, This is my first post. It's so easy!")
        expected_post_2 = Post(2, "New Post", "Wow, these guys deserve an A++")
        expected_post_3 = Post(3, "Latest Post", "Wow, these devs are so intelligent!")
        
        empty_list = blog.retrieve_posts("legend")
        self.assertEqual(0, len(empty_list))
        
        first_list = blog.retrieve_posts("first")
        self.assertEqual(1, len(first_list))

        actual_post_1 = first_list[0]
        self.assertEqual(expected_post_1, actual_post_1)

        full_list = blog.retrieve_posts("Wow")
        actual_post_2 = full_list[1]
        actual_post_3 = full_list[2]
        
        self.assertEqual(expected_post_2, actual_post_2)
        self.assertEqual(expected_post_3, actual_post_3)
        


if __name__ == '__main__':
    unittest.main()
