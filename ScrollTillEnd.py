import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.ajio.com/s/clothing-4461-74582")

height = driver.execute_script("return document.body.scrollHeight")
# print("height", height)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("new_height", new_height)
    print("height", height)
    if height == new_height:
        break
    height = new_height
