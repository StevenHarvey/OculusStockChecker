import time
import phonenoti
import requests
import lxml
from bs4 import BeautifulSoup
url = 'https://www.oculus.com/quest/?locale=en_US'
r = requests.get(url)
html_content = r.text
i = 0
foo = 0
def run():
    soup = BeautifulSoup(html_content, "lxml")
    soupconf = (soup.find_all('button')[0:1])
    if "Out of Stock" in str(soupconf):
        end()
    elif "Out of Stock" not in str(soupconf):
        phonenoti.send_notification_via_pushbullet("THEYRE IN STOCK!", "BREAKING!, The Oculus Quest is in stock!, Click here to go to the website - https://www.oculus.com/quest/?locale=en_US")
    else:
        print("Fatal Error")
def end():
    global i
    if i < 1 and foo <= 0:
        print("Counter Started!")
        i += 1
        run()
    else:
        time.sleep(60)
        i += 1
        print("Code has run "+ str(i)+" times")
        run()
end()
