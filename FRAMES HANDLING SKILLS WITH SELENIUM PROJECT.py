# ---------------------------------------------------------------
# Selenium Automation Script: Handling Frames (iFrame)
# ---------------------------------------------------------------
# Author: Anup Sharma
# Purpose: Demonstrates how to automate interactions inside an iframe
#          using Selenium WebDriver with Firefox browser.
# Skills Shown:
#   - WebDriver setup and configuration
#   - Frame (iframe) handling in Selenium
#   - Clearing and entering text in an editable area
#   - Switching between frames and default content
# ---------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize Firefox WebDriver instance
driver = webdriver.Firefox()

# Set implicit wait for 10 seconds to allow elements to load
driver.implicitly_wait(10)

# Maximize browser window for better visibility
driver.maximize_window()

# Navigate to test webpage with iframe
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to the iframe using its ID
driver.switch_to.frame("mce_0_ifr")

# Clear existing text inside the editable TinyMCE editor
driver.find_element(By.ID, "tinymce").clear()

# Enter custom text into the editor
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

# Switch back to the main/default page content
driver.switch_to.default_content()  # NOTE: Typo in 'switch' — adjust if needed

# Retrieve and print the heading text (for assertion or verification)
print(driver.find_element(By.CSS_SELECTOR, "h3").text)  # NOTE: Typo in 'CSS_SELECTOR'

# Wait 5 seconds before closing browser (to observe results)
time.sleep(5)
#result will be error becuse the site dont allow the edit option without any package so error come