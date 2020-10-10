import requests
from bs4 import BeautifulSoup
url = 'https://www.oculus.com/quest/?locale=en_US'
r = requests.get(url)
html_content = r.text
def run():
    soup = BeautifulSoup(html_content, "html5lib")
    soupconf = (soup.find_all('button')[0:1])
    if "Out of Stock" in str(soupconf):
        print("Out of Stock")
    elif "Out of Stock" not in str(soupconf):
        print("IN STOCK")
    else:
        print("Fatal Error")
