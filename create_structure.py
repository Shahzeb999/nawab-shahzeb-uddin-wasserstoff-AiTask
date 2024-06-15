import os

# Define the project structure
project_structure = {
    "project_name": "chatbot_project",
    "folders": [
        "chatbot_project",
        "chatbot_project/static",
        "chatbot_project/templates",
        "chatbot_project/app",
        "chatbot_project/app/api",
        "chatbot_project/app/models",
        "chatbot_project/app/templates",
        "chatbot_project/app/static",
        "chatbot_project/app/utils",
    ],
    "files": {
        "chatbot_project": ["run.py", ".env"],
        "chatbot_project/app": ["__init__.py", "views.py"],
        "chatbot_project/app/api": ["__init__.py", "chatbot_api.py"],
        "chatbot_project/app/models": ["__init__.py"],
        "chatbot_project/app/templates": [],
        "chatbot_project/app/static": [],
        "chatbot_project/app/utils": ["__init__.py"],
    },
    "templates": {
        "run.py": """from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
""",
        "app/__init__.py": """from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .api import chatbot_api
    app.register_blueprint(chatbot_api.bp)

    from .views import main
    app.register_blueprint(main.bp)

    return app
""",
        "app/views.py": """from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
""",
        "app/api/chatbot_api.py": """from flask import Blueprint, request, jsonify

bp = Blueprint('chatbot_api', __name__)

@bp.route('/api/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get("query")
    # Process the query and generate a response
    response = {"response": f"Received query: {user_query}"}
    return jsonify(response)
""",
        ".env": """FLASK_APP=run.py
FLASK_ENV=development
""",
        "config.py": """class Config:
    SECRET_KEY = 'your_secret_key'
    # Add other configuration variables as needed
"""
    }
}

# Function to create directories
def create_directories(base_path, folders):
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Function to create files with templates
def create_files(base_path, files, templates):
    for folder, filenames in files.items():
        for filename in filenames:
            file_path = os.path.join(base_path, folder, filename)
            with open(file_path, 'w') as f:
                template_content = templates.get(f"{folder}/{filename}", "")
                f.write(template_content)

# Base path for the project
base_path = os.getcwd()

# Create directories
create_directories(base_path, project_structure["folders"])

# Create files with templates
create_files(base_path, project_structure["files"], project_structure["templates"])

print("Project structure created successfully!")
