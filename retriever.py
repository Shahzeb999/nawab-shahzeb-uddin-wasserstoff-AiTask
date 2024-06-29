import requests

url = 'https://wordpress.com/blog/2024/06/20/wceu-2024/'

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

# Fetch and print the content
content = fetch_content(fetch_url)
