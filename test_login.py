from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome for GitHub Actions
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Launch Chrome
driver = webdriver.Chrome(options=options)

try:
    # Open website
    driver.get("https://www.saucedemo.com")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Verify login
    if "inventory" in driver.current_url:
        print("✅ Login test PASSED")
    else:
        print("❌ Login test FAILED")

finally:
    driver.quit()