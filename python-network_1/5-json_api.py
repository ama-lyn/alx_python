'''
a Python script that takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys

if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
response = requests.post(url, data={'q': q})

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
