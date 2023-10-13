import builtwith
import requests
from bs4 import BeautifulSoup


email = input('Enter the email address : ')

domain = email.split('@')[1]

url = 'https://' + domain
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
technologies = builtwith.builtwith(url)
print(technologies)
