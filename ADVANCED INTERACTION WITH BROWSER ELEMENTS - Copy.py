# ------------------------------------------------------------
# Project: Hover Actions Automation (Selenium)
# File: hover_actions_automation.py
# Description:
#   Small demo script that shows how to perform mouse-hover,
#   context-click (right-click) and clicking submenu items using
#   Selenium's ActionChains on the AutomationPractice demo page.
#
# Purpose for Recruiters:
#   - Demonstrates WebDriver setup and configuration
#   - Shows use of ActionChains for complex mouse interactions
#   - Uses different element locators (ID, LINK_TEXT)
#   - Uses implicit waits and browser window maximization for stability
#
# Note: Code logic is preserved exactly as original — only comments
#       added for clarity and presentation on GitHub.
# ------------------------------------------------------------

# (left intentionally as in original file)
from pydoc import text

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize Chrome WebDriver (make sure chromedriver is in PATH or configured)
driver = webdriver.Chrome()

# Set a global implicit wait — allows Selenium to poll DOM for elements up to 5 seconds
driver.implicitly_wait(5)

# Maximize the browser window to ensure elements are visible and consistent for tests
driver.maximize_window()

# Navigate to the demo page that contains hover/menu actions
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Prepare ActionChains instance to perform complex mouse interactions
# (ActionChains class is imported above; the standalone ActionChains line is kept from original)
ActionChains
action = ActionChains(driver)

# You can perform different actions using ActionChains:
# - click_and_hold()
# - double_click()
# - context_click()   -> right click
# - drag_and_drop()   -> requires source and target elements
# In this script we will demonstrate hover, right-click, and clicking a submenu.

# Move mouse to the element with ID "mousehover" to reveal the hidden submenu
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# Perform a context-click (right click) on the "Top" link that appears under the hover menu
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

# Move to the "Reload" link and click it — demonstrates chaining move + click in one sequence
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# Wait so the tester can visually confirm the actions (kept as in original code)
time.sleep(10)

# End of script (driver not closed here because original code didn't include quit())
# If you want to gracefully close the browser after verification, add:
# driver.quit()
