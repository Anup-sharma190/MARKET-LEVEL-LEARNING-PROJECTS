"""
Project Title: Selenium Automation – Switching Between Parent & Child Windows/Tabs

Description:
This project demonstrates how to handle multiple browser windows/tabs using Selenium WebDriver in Python.
It covers switching control from a parent window to a newly opened child window, extracting data from it,
and then switching back to the parent window. This is a common automation scenario for testers and QA engineers
when working with applications that open popups or external links.

Key Skills & Concepts:
- Selenium WebDriver automation
- Handling multiple windows/tabs
- Using window handles for navigation
- Locating elements with different locators (By.LINK_TEXT, By.TAG_NAME)
- Python scripting for QA automation
- Basic synchronization using time.sleep()

Use Case:
Many real-world applications open new browser tabs or pop-up windows for forms, payment gateways, or documentation.
Automating the process of switching between these windows ensures smooth end-to-end testing and validation.

Tools & Technologies:
- Python 3.x
- Selenium WebDriver
- Google Chrome Browser
- ChromeDriver

Author: Anup Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#  Create a Chrome driver instance
driver = webdriver.Chrome()

# Open the URL
driver.get("https://the-internet.herokuapp.com/windows")

# Click the link to open new window
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(10)

# Get all window handles
open_windows = driver.window_handles

# Switch to the new window
driver.switch_to.window(open_windows[1])

# Print the text from new window
print(driver.find_element(By.TAG_NAME, "h3").text)  # new window

# Close the child window
driver.close()  # IT WILL CLOSE ONLY CHILD WINDOW

# Switch back to the parent window
driver.switch_to.window(open_windows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text  # verify text in parent window

time.sleep(5)
driver.quit()
