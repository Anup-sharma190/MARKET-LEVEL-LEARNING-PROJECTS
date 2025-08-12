# ---------------------------------------------------------------
# Selenium Automation Script: Handling Frames (iFrame)
# ---------------------------------------------------------------
# Author       : Anup Sharma
# Date         : 12-Aug-2025
# Purpose      : Demonstrates how to automate interactions inside an iframe
#                using Selenium WebDriver with Chrome browser.
# Skills Shown :
#   - WebDriver setup and configuration
#   - Navigating to a webpage and scrolling
#   - Handling iframes (switching in/out)
#   - Capturing webpage screenshots
# ---------------------------------------------------------------
# Pre-requisites:
#   pip install selenium
#   Chrome browser must be installed
# ---------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -------------------- Step 1: Initialize Chrome WebDriver --------------------
# Configure Chrome to run in headless mode and ignore certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run without opening browser window
chrome_options.add_argument("--ignore-certificate-errors")

# Create WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# -------------------- Step 2: Set implicit wait --------------------
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

# -------------------- Step 3: Maximize window (optional) --------------------
driver.maximize_window()

# -------------------- Step 4: Open target webpage --------------------
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# -------------------- Step 5: Scroll to the bottom --------------------
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(1)  # Small pause to ensure scroll completes

# -------------------- Step 6: Capture screenshot --------------------
driver.get_screenshot_as_file("screen.png")
print("Screenshot saved as 'screen.png'.")

# -------------------- Step 7: Close the browser --------------------
driver.quit()
print("Test completed successfully.")
