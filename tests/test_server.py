import unittest
from app import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_update_embeddings(self):
        response = self.app.post('/update_embeddings', json={'post_id': 1, 'post_content': 'Sample content'})
        self.assertEqual(response.status_code, 200)

    def test_process_query(self):
        response = self.app.post('/process_query', json={'query': 'Why is the sky blue?'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
