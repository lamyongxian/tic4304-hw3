from urllib.parse import urlencode
from urllib.request import Request, urlopen
import hashlib, requests

url = 'http://www.wsb.com/Homework3/case03/register.php'
# Prepare registration POST
hashpwd = hashlib.sha512('123456'.encode()).hexdigest()
values = dict(username='test', email='test@test.com', p=hashpwd)
data = urlencode(values).encode()
# Submit the registration
req = Request(url, data)
rsp = urlopen(req)

# Start Session to store cookies
s = requests.Session()

# Login
url2 = 'http://www.wsb.com/Homework3/case03/includes/process_login.php'
login = s.post(url2, data={'email': 'test@test.com', 'p': hashpwd})

# Load protected page
url3 = 'http://www.wsb.com/Homework3/case03/protected_page.php?admin=true'
content = s.get(url3)

#read the return result
#content = rsp2.read().decode()

#print(login.text)
print(content.text)

#import webbrowser
#url = "http://www.wsb.com/Homework3/case01.php"
#new = 2 #open in new window
#webbrowser.open(url,new=new)
