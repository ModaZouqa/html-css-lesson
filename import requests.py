import requests 
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/SnapStreaks/comments/gjew0f/join_snap_spam_group_to_increase_snap_score/'

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Get the target element
target_element = soup.find("p", class_="_1qeIAgB0cPwnLhDF9XSiJM")

# Print the text attribute
print(target_element.text)
