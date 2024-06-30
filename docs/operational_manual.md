# Operational Manual

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask server: `python ai/server.py`
4. Install the WordPress plugin by copying the `wordpress_plugin` directory to the `wp-content/plugins` directory.

## Configuration
- Update API keys in `ai/embeddings.py` and `ai/rag_cot.py`.

## Troubleshooting
- Check Flask server logs for errors.
- Ensure WordPress REST API routes are accessible.
