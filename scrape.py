import requests
from bs4 import BeautifulSoup

# Make a GET request to the URL
response = requests.get('https://www.reddit.com/r/SnapStreaks/comments/gjew0f/join_snap_spam_group_to_increase_snap_score/')

# Parse the HTML of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element with the class "_1qeIAgB0cPwnLhDF9XSiJM"
element = soup.find('p', class_='_1qeIAgB0cPwnLhDF9XSiJM')

# Print the text content of the element
print(element.text)