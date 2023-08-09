'''
Module that imports request package and retrieves 
data from the url and perform some functions on the
data to get a better understanding of how it works
'''
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)


if response.status_code == 200:
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
else:
    print("Error:", response.status_code)
