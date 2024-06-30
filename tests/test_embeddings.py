import unittest
from ai.embeddings import generate_embeddings

class TestEmbeddings(unittest.TestCase):
    def test_generate_embeddings(self):
        text = "Sample text for embedding generation."
        embeddings = generate_embeddings(text)
        self.assertIsNotNone(embeddings)

if __name__ == '__main__':
    unittest.main()
