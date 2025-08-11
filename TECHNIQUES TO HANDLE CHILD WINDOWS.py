"""
======================================================
Project: Handling Multiple Browser Windows in Selenium
Author: Anup Sharma
Description:
    This project demonstrates how to handle multiple
    browser windows or tabs using Selenium WebDriver.

    Key Concepts Covered:
    - Launching a browser with Selenium
    - Opening and switching between browser windows
    - Extracting text from both child and parent windows
    - Closing specific windows and returning to the main one
======================================================
"""

# Import necessary Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Step 2: Open the test website
driver.get("https://the-internet.herokuapp.com/windows")

# Step 3: Click the link to open a new browser window
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)  # Wait to ensure new window opens

# Step 4: Get the list of all open window handles (IDs)
open_windows = driver.window_handles

# Step 5: Switch to the child window (index 1)
driver.switch_to.window(open_windows[1])

# Step 6: Extract and print text from the child window
print(driver.find_element(By.TAG_NAME, "h3").text)  # Expected: "New Window"

# Step 7: Close the child window
driver.close()

# Step 8: Switch back to the parent window (index 0)
driver.switch_to.window(open_windows[0])

# Step 9: Validate the parent window text
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

# Step 10: Wait briefly before quitting the browser
time.sleep(2)
driver.quit()
