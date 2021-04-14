from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



driver = webdriver.Chrome("chromedriver.exe")
driver.set_page_load_timeout("15")

user = "test@gmail.com"
pwd = "test123"

driver.maximize_window()

driver.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

time.sleep(1)


searchEmail = driver.find_element_by_id("identifierId") #whsOnd zHQkBf whsOnd zHQkBf
searchEmail.send_keys(user)

print ("Email Id entered")
time.sleep(1)


nextButton = driver.find_element_by_id('identifierNext')
nextButton.click()


searchPassword = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
searchPassword.send_keys(pwd)

time.sleep(5)
print ("Password Id entered")
time.sleep(1)

signInButton = driver.find_element_by_id('passwordNext')
signInButton.click()

time.sleep(10)


spamFolder = driver.find_element_by_css_selector("[title='Spam']")

spamFolder.click()

time.sleep(10)

#AllCheckBox = driver.find_element_by_id(":k8")

AllCheckBoxDropDown = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, ':nh')))
#AllCheckBoxDropDown = driver.find_element_by_css_selector("span.T-JoJ-J5-Ji")

#AllCheckBox = driver.find_element_by_css_selector(".J-J5-Ji.J-JN-M-I-Jm")
AllCheckBoxDropDown.click()

time.sleep(5)


#AllCheckBox = driver.find_element_by_css_selector("[selector='all']")
#AllCheckBox.click()

#time.sleep(5)
NotSpamAll = driver.find_element_by_css_selector(".T-I.J-J5-Ji.aFk.T-I-ax7.mA")
NotSpamAll.click()

time.sleep(5)

#signOutButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gb_B.gb_Da.gb_g")))

signOutButton = driver.find_element_by_css_selector(".gb_B.gb_Da.gb_g")

signOutButton.click()

time.sleep(3)
logout1=driver.find_element_by_id("gb_71") #error in this line
logout1.click()

#time.sleep(20)


driver.quit()
