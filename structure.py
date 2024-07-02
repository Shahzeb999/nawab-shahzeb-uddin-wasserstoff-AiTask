import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

# Define the base directory for the plugin
base_dir = "wp-content/plugins/rag-chatbot"

# Create the main plugin directory
create_directory(base_dir)

# Create subdirectories
subdirs = [
    "includes",
    "admin/css",
    "admin/js",
    "admin/partials",
    "public/css",
    "public/js",
    "public/partials",
    "languages"
]

for subdir in subdirs:
    create_directory(os.path.join(base_dir, subdir))

# Create main files
files = [
    "rag-chatbot.php",
    "readme.txt",
    "includes/class-rag-chatbot.php",
    "includes/class-settings.php",
    "includes/functions.php",
    "admin/css/admin.css",
    "admin/js/admin.js",
    "admin/partials/settings-page.php",
    "public/css/public.css",
    "public/js/chatbot.js",
    "public/partials/chatbot-widget.php",
    "languages/rag-chatbot.pot"
]

for file in files:
    create_file(os.path.join(base_dir, file))

print("Plugin structure created successfully!")