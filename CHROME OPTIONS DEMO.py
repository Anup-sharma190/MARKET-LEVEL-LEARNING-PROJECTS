"""
Selenium Automation Script - Web Page Title Extractor
------------------------------------------------------

Project Overview:
This script uses Selenium WebDriver to open a target webpage and print its title.
It demonstrates basic Selenium automation steps: initializing the WebDriver,
configuring Chrome options, navigating to a webpage, and retrieving page information.

Tools & Technologies:
- Python 3
- Selenium WebDriver
- Google Chrome & ChromeDriver

Skills Demonstrated:
- Web automation and browser interaction
- Use of Chrome WebDriver options
- Headless browser execution for faster automation
- Basic debugging and page title extraction

Author: Anup Sharma
Date: August 2025
"""

# -------------------- Step 1: Import Required Libraries --------------------
from selenium import webdriver
from selenium.webdriver.common.by import By  # For locating elements (not used here but kept for reference)
import time

# -------------------- Step 2: Configure Chrome WebDriver --------------------
chrome_options = webdriver.ChromeOptions()

# Run Chrome in headless mode (no browser window)
chrome_options.add_argument("--headless")

# Start browser maximized
chrome_options.add_argument("--start-maximized")

# Ignore SSL errors (optional, useful for certain test sites)
chrome_options.add_argument("--ignore-certificate-errors")

# -------------------- Step 3: Initialize WebDriver --------------------
driver = webdriver.Chrome(options=chrome_options)

# -------------------- Step 4: Open Target Web Page --------------------
driver.get("https://rahulshettyacademy.com/angularpractice/")

# -------------------- Step 5: Retrieve and Print Page Title --------------------
page_title = driver.title
print(f"Web Page Title: {page_title}")

# -------------------- Step 6: Close the Browser --------------------
driver.quit()
