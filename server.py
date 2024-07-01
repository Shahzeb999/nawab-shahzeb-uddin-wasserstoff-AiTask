from flask import Flask, request, jsonify, render_template
import logging
from ai.database_update import update_vector_database
from ai.rag_cot import process_query_with_chain_of_thought

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Global variable for the index
index = None

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/update_embeddings', methods=['POST'])
def update_embeddings():
    global index
    try:
        data = request.json
        url = data['url']
        
        # Validate input
        if not url:
            raise ValueError("URL must be provided")
        
        index = update_vector_database(url)
        return jsonify({'status': 'success', 'message': 'Index updated successfully'}), 200
    except Exception as e:
        logging.error(f"Error updating embeddings: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/process_query', methods=['POST'])
def process_query():
    global index
    try:
        data = request.json
        user_query = data['query']
        previous_context = data['previous_context']
        
        # Validate input
        if not user_query:
            raise ValueError("User query must be provided")

        if index is None:
            raise ValueError("Index is not initialized. Update embeddings first.")
        
        response = process_query_with_chain_of_thought(user_query, previous_context, index)
        return jsonify({'response': response}), 200
    except Exception as e:
        logging.error(f"Error processing query: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)