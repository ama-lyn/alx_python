#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request 
to the URL and displays the value of the variable X-Request-Id 
in the response header
'''
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)


if 'X-Request-Id' in response.headers:
    request_id = response.headers['X-Request-Id']
    print(request_id)
