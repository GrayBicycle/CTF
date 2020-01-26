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
    
def get_text(bin_text):
    return "".join(chr(int(bin_text[i*8:i*8+8], 2)) for i in range(len(bin_text)//8))


session = requests.Session()
data = {"username":"GrayBicycle", "password":"!Tango021"}
url = "https://ringzer0ctf.com/login"
response = session.post(url, data=data)

challenge = "https://ringzer0ctf.com/challenges/14"
response = session.post(challenge)

message = get_head(response._content)[2].strip()
message = get_text(message)
encodeMessage = hashlib.sha512(message.encode("utf-8")).hexdigest()

challenge = "https://ringzer0ctf.com/challenges/14/" + encodeMessage
response = session.post(challenge)

flag = re.search(r"FLAG-([a-zA-Z]|\d)*", response._content.decode())
print(flag.group(0))