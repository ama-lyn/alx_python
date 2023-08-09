'''
Module that contains a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response.
'''

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print("Your email is:", email)
print(response.text)
