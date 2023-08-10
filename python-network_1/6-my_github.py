'''
A Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
'''
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    try:
        print(r.json().get('id'))
    except ValueError:
        print('Not a valid JSON')
