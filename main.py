import time
from selenium import webdriver
from bs4 import *
import classifybuttons as cb

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get('https://www.ing.com.au/securebanking/');
soup = BeautifulSoup(driver.page_source, "html.parser")

mydivs = soup.findAll("img",  class_="style-scope ing-keypad")
mapping = []
for div in mydivs:

    #print(div['src'])
    mapping.append(cb.classify_image(bytes(div['src'], encoding="ascii")))

cif = driver.find_element_by_id("cifField")
cif.send_keys("00000000")


def clickPIN(l):
    for num in l:
        driver.execute_script("document.querySelector('.uia-pin-" + str(mapping.index(str(num)))  +"').click()")
        time.sleep(1)
time.sleep(2)

clickPIN([1,2,3,4])
submit = driver.find_element_by_id("login-btn")
submit.click()
time.sleep(2)

driver.execute_script("document.querySelector('a .style-scope .ing-all-accounts-summary').click()")
time.sleep(3)
driver.execute_script("document.querySelector('[data-id=ofx]').click()")