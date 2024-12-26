import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://github.com'

# Fetch the content of the page
response = requests.get(url)

# Check for successful request
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the page title
    print("Page Title:", soup.title.string)
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")