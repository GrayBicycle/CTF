import re
import hashlib
import requests
from bs4 import BeautifulSoup 

def get_head(html):
    soup = BeautifulSoup(html,'lxml')
    head = soup.find('div', class_='message')
    heads = []

    for i in head:
        heads.append(i.string)
    return heads   
    
session = requests.Session()
data = {"username":"", "password":""} #input your login and pass
url = "https://ringzer0ctf.com/login"
response = session.post(url, data=data)

challenge = "https://ringzer0ctf.com/challenges/13"
response = session.post(challenge)

message = get_head(response._content)[2].strip()

encodeMessage = hashlib.sha512(message.encode("utf-8")).hexdigest()

challenge = "https://ringzer0ctf.com/challenges/13/" + encodeMessage
response = session.post(challenge)

flag = re.search(r"FLAG-([a-zA-Z]|\d)*", response._content.decode())
print(flag.group(0))


