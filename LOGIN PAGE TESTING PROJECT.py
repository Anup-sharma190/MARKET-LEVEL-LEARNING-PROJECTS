"""
Project: Basic Login Automation with Selenium (Smoke Test)

Short description:
This simple script demonstrates an automated smoke test for a web application's
login flow using Selenium WebDriver (Python). It launches Chrome, navigates to
the login page, types credentials, clicks the login button, verifies whether
the dashboard loaded (by checking the page title), and then closes the browser.

Notes for recruiters:
- Purpose: quick sanity check (smoke test) for login functionality.
- This is a minimal example useful to demonstrate end-to-end browser automation.
- Replace the URL and locator values with your application's actual values before use.

Author: Anup Sharma
Tech stack: Python 3.x, Selenium WebDriver, ChromeDriver
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Open real login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait until username field is visible
wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))

# Enter credentials
username_input.send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# Verify result
if "Logged In Successfully" in driver.page_source:
    print("✅ Login Test Passed")
else:
    print("❌ Login Test Failed")

# Close browser
driver.quit()
