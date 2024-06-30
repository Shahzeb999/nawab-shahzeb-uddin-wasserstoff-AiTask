import unittest
from ai.retriever import create_vector_index

class TestRetriever(unittest.TestCase):
    def test_create_vector_index(self):
        urls = ['https://wordpress.com/blog/2024/06/19/security-scanning/']
        index = create_vector_index(urls)
        self.assertIsNotNone(index)

if __name__ == '__main__':
    unittest.main()
