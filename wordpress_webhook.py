import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordpress_content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing WordPress posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wp_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False)
    modified = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(300))
    categories = db.Column(db.String(300))
    tags = db.Column(db.String(300))

# Create database tables
with app.app_context():
    db.create_all()

# Webhook endpoint for receiving updates from WordPress
@app.route('/webhook/wordpress', methods=['POST'])
def wordpress_webhook():
    data = request.json
    
    # Validate the incoming data (implement your own validation logic)
    if not data or 'id' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # Update or create post in database
    post = Post.query.filter_by(wp_id=data['id']).first()
    if post:
        # Update existing post
        post.title = data['title']
        post.content = data['content']
        post.excerpt = data.get('excerpt', '')
        post.author = data['author']
        post.date = datetime.fromisoformat(data['date'])
        post.modified = datetime.fromisoformat(data['modified'])
        post.url = data['url']
        post.categories = ','.join(data['categories'])
        post.tags = ','.join(data['tags'])
    else:
        # Create new post
        post = Post(
            wp_id=data['id'],
            title=data['title'],
            content=data['content'],
            excerpt=data.get('excerpt', ''),
            author=data['author'],
            date=datetime.fromisoformat(data['date']),
            modified=datetime.fromisoformat(data['modified']),
            url=data['url'],
            categories=','.join(data['categories']),
            tags=','.join(data['tags'])
        )
        db.session.add(post)

    db.session.commit()

    # Send data to chatbot backend
    send_to_chatbot_backend(data)

    return jsonify({'success': True}), 200

# Function to send data to chatbot backend
def send_to_chatbot_backend(data):
    chatbot_api_url = 'https://your-chatbot-backend.com/api/update-content'
    try:
        response = requests.post(chatbot_api_url, json=data)
        response.raise_for_status()
        app.logger.info(f"Successfully sent post data to chatbot backend for post ID: {data['id']}")
    except requests.RequestException as e:
        app.logger.error(f"Error sending post data to chatbot backend: {str(e)}")

# API endpoint for fetching recent content
@app.route('/api/recent-content', methods=['GET'])
def get_recent_content():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    posts = Post.query.order_by(Post.modified.desc()).paginate(page=page, per_page=per_page, error_out=False)

    result = []
    for post in posts.items:
        result.append({
            'id': post.wp_id,
            'title': post.title,
            'content': post.content,
            'excerpt': post.excerpt,
            'author': post.author,
            'date': post.date.isoformat(),
            'modified': post.modified.isoformat(),
            'url': post.url,
            'categories': post.categories.split(','),
            'tags': post.tags.split(',')
        })

    return jsonify({
        'posts': result,
        'total': posts.total,
        'pages': posts.pages,
        'current_page': page
    })

if __name__ == '__main__':
    app.run(debug=True)