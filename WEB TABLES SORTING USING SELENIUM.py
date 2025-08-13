"""
====================================================================================
PROJECT NAME : Web Table Sorting Validation using Selenium
AUTHOR       : Anup Sharma
DESCRIPTION  :
    This automation script verifies that the "Veg/fruit name" column in a web table
    is sorted in ascending order after clicking its column header.

OBJECTIVE:
    - Open the Offers page of the sample Selenium practice site.
    - Click on the column header "Veg/fruit name" to sort the table.
    - Capture all vegetable/fruit names from the first column.
    - Compare the order of items in the browser with a Python-sorted list.
    - Validate that the sorting feature on the website works correctly.

TOOLS & TECHNOLOGIES:
    - Python 3.x
    - Selenium WebDriver
    - Chrome WebDriver

SKILLS DEMONSTRATED:
    - Selenium automation scripting
    - Locating elements using XPath
    - Web table data extraction
    - Python list handling and sorting
    - Test validation using assertions
    - Headless browser execution for faster tests

USAGE:
    Ensure ChromeDriver is installed and available in your PATH.
    Run this script using:
        python "WEB TABLES SORTING USING SELENIUM.py"

====================================================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -------------------- Step 1: Initialize Chrome WebDriver --------------------
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Optional: run without opening the browser window
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)

# -------------------- Step 2: Open the target web page --------------------
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# -------------------- Step 3: Prepare a list to store items from the browser --------------------
browsersortedveggies = []

# -------------------- Step 4: Click on the "Veg/fruit name" column header to sort --------------------
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# -------------------- Step 5: Capture all items from the first column --------------------
veggiewebelements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggiewebelements:
    browsersortedveggies.append(ele.text)

# -------------------- Step 6: Keep a copy of the original list from the browser --------------------
originalbrowsersortedlist = browsersortedveggies.copy()

# -------------------- Step 7: Sort the list in Python and compare with the browser's list --------------------
browsersortedveggies.sort()
assert browsersortedveggies == originalbrowsersortedlist, "Sorting order mismatch!"

# -------------------- Step 8: Close the browser --------------------
driver.quit()

# -------------------- Step 9: Print success message --------------------
print("Test completed successfully. Web table is sorted correctly.")
print(browsersortedveggies)
