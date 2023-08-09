'''
A module that contains a Python script that takes in a URL, sends a request 
to the URL and displays the value of the variable X-Request-Id 
in the response header
'''
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)


if response.status_code == 200:
    print(response.headers['X-Request-Id'])
