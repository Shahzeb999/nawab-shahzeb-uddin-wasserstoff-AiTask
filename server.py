from flask import Flask, request, jsonify
from ai.embeddings import generate_embeddings
from ai.rag_cot import process_query_with_chain_of_thought
from ai.retriever import create_vector_index, update_vector_database
import logging
import requests

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

def fetch_content_from_url(url):
    # Implement content fetching logic
    
    import requests


# URL to fetch the content from

def fetch_content(url):

    fetch_url = f'https://r.jina.ai/{url}'

    try:
        # Make GET request to the provided URL
        response = requests.get(fetch_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            content = response.text
            print(content)
        else:
            print(f"Error retrieving content: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return content



@app.route('/update_embeddings', methods=['POST'])
def update_embeddings():
    try:
        data = request.json
        url = data['url']
        
        # Validate input
        if not url:
            raise ValueError("URL must be provided")

        # Fetch content from the URL
        post_content = fetch_content_from_url(url)

        # Generate embeddings
        embeddings = generate_embeddings(post_content)

        # Update vector database with embeddings
        update_vector_database(url, embeddings)

        return jsonify({'status': 'success'}), 200
    except Exception as e:
        logging.error(f"Error updating embeddings: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/process_query', methods=['POST'])
def process_query():
    try:
        data = request.json
        user_query = data['query']
        previous_context = data.get('previous_context', '')
        
        # Validate input
        if not user_query:
            raise ValueError("User query must be provided")

        response = process_query_with_chain_of_thought(user_query, previous_context)
        return jsonify({'response': response}), 200
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
