import requests
import sys

'''
Module that contains a a Python script that takes in a URL,
sends a request to the URL and displays the body of the 
response.
'''

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
