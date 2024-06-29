import os

# Define the directory structure
directories = [
    "rag-chatbot/",
    "rag-chatbot/ai",
    "rag-chatbot/wordpress_plugin",
    "rag-chatbot/wordpress_plugin/api",
    "rag-chatbot/tests",
    "rag-chatbot/docs"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Define the files and their initial content
files_content = {
    "rag-chatbot/ai/__init__.py": "",
    "rag-chatbot/ai/embeddings.py": "",
    "rag-chatbot/ai/rag_cot.py": "",
    "rag-chatbot/ai/retriever.py": "",
    "rag-chatbot/ai/server.py": "",
    "rag-chatbot/wordpress_plugin/chatbot-plugin.php": "",
    "rag-chatbot/wordpress_plugin/api/index.php": "",
    "rag-chatbot/wordpress_plugin/api/fetch_content.php": "",
    "rag-chatbot/wordpress_plugin/api/update_embeddings.php": "",
    "rag-chatbot/tests/test_embeddings.py": "",
    "rag-chatbot/tests/test_rag_cot.py": "",
    "rag-chatbot/tests/test_retriever.py": "",
    "rag-chatbot/tests/test_server.py": "",
    "rag-chatbot/docs/system_design.md": "",
    "rag-chatbot/docs/operational_manual.md": "",
    "rag-chatbot/docs/project_report.md": "",
    "rag-chatbot/requirements.txt": "",
    "rag-chatbot/README.md": ""
}

# Create the files with initial content
for file_path, content in files_content.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Project structure created successfully.")
