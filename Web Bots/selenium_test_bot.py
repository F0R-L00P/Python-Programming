# import webdrive, this allows for web interaction
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # have access to keys such as Enter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

# get path to the file and the file name (.exe)
PATH = r'C:\Users\behna\Downloads\chromedriver_win32\chromedriver.exe'

# pick the browser to be used
# add driver path
# add options to disable pop-ups
IP = ['36.100.148.123',
      '143.248.237.197',
      '252.45.142.175',
      '51.84.90.129',
      '4.136.125.151',
      '178.38.3.11',
      '121.150.237.158',
      '10.208.181.130',
      '7.31.110.232',
      '108.119.226.195',
      '24.35.84.230',
      '29.88.54.210',
      '62.160.82.119',
      '121.31.98.181',
      '22.236.26.162']

user = random.choice(IP)
p_ups = "--disable-notifications"
privacy = "--incognito"

options = Options()
options.add_argument(user)
options.add_argument(p_ups)
#options.add_argument(privacy)
#options.add_argument('headless')


driver = webdriver.Chrome(PATH, options=options)

# put in name of any web that we are interested to search
time.sleep(2)

driver.get('https://www.upwork.com/ab/account-security/login')

time.sleep(1)

# obtain webpage tile before proceeding
assert "Log In - Upwork" in driver.title

# to access elemnt on a webpage inspect the page and the target element
# when searching for elements, do it by ID first
# if id not available do it by NAME

# you can use find to isolate target by name, id, etc..
search = driver.find_element_by_id("login_username")

time.sleep(2)
    
# return object representing the search bar to interact with
search.clear() # clear the search bar if any text is pre-populated
search.send_keys('EMAIL', Keys.TAB) # type email in the search bar
search.send_keys(Keys.RETURN) # hit enter and search for test

time.sleep(2)

search = driver.find_element_by_id("login_password") # filing password information
search.send_keys('PASSWORD', Keys.TAB * 3) # type test in the search bar
search.send_keys(Keys.RETURN) # hit enter and search for test

time.sleep(2)

# Explicit Waits
# can delay selenium for a specified time before proceeding with the code
# this will ensure that the material exists in the page for us to move forward

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='gw-c-mobile-app-banner']/div/div/div/button"))).click()
except:
    pass

time.sleep(1)

# click on messages
search = driver.find_element_by_xpath("//*[@id='nav-right']/ul/li[4]").click() 

# click on call button
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='calls-menu']/button"))).click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='calls-menu']/ul/li[1]/a"))).click()
except:
    pass


# you can either close the tab using 
#driver.close()

# or close the entire window using 
driver.quit()