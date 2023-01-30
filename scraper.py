import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://techcrunch.com')
time.sleep(5)
link = driver.find_element(By.CLASS_NAME, 'post-block__title__link')
link.click()

url = requests.get(driver.current_url)

soup = BeautifulSoup(url.content, 'html.parser')

heading1 = soup.find('h1', class_='article__title').text

img = soup.find('img', class_='article__featured-image').get('src')

d = urllib.request.urlretrieve(img, 'img.jpg')
p = soup.find('div', class_='article-content')
content = p.find_all('p')
for ltext in content:
    print(ltext.text)
time.sleep(10)

driver.get('https://gwaliorgeeks.com/admin/login/?next=/admin/')
time.sleep(3)
username = driver.find_element(By.NAME,'username')
username.send_keys('annex360')

password = driver.find_element(By.NAME,'password')
password.send_keys('annex360')

time.sleep(3)
submit = driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input')
submit.click()
time.sleep(10)
driver.close()
