import unittest
from ai.rag_cot import process_query_with_chain_of_thought

class TestRAGCoT(unittest.TestCase):
    def test_process_query(self):
        response = process_query_with_chain_of_thought("Why is the sky blue?", "")
        self.assertIn("Refined response:", response)

if __name__ == '__main__':
    unittest.main()
