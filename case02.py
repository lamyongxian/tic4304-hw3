import requests

url = 'http://www.wsb.com/Homework3/case02.php'

res = requests.get(url, allow_redirects=False)

print(res.text)

