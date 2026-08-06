from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # download and install the compatible ChromeDriver binary automatically 
import time # pause

# Open Chrome
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service) # helps to automatically manage the ChromeDriver binary

# Go to the site
driver.get("https://www.saucedemo.com") # typing the url into the browser and hitting enter

# Type into username and password boxes
driver.find_element(By.ID, "user-name").send_keys("standard_user") # By - find particular element on the page
driver.find_element(By.ID, "password").send_keys("secret_sauce") 

# Click login
driver.find_element(By.ID, "login-button").click() # by default, Selenium will wait for the page to load before moving on to the next line of code

time.sleep(2)  # just so you can SEE it worked

# Check we landed on the right page
if "inventory" in driver.current_url: # check if the current URL contains "inventory"
    print("✅ Login test PASSED")
else:
    print("❌ Login test FAILED")

driver.quit() # close the browser window and end the WebDriver session