from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Initialize WebDriver (using Chrome here)
driver = webdriver.Chrome()

# Step 2: Open Wikipedia
driver.get("https://www.wikipedia.org")

# Step 3: Small wait for page to load
time.sleep(2)

# Step 4: Find the search box using By.ID
search_box = driver.find_element(By.ID, "searchInput")

# Step 5: Type a query into the search box
search_box.send_keys("Python programming language")

# Step 6: Press ENTER
search_box.send_keys(Keys.RETURN)

# Step 7: Wait to see results
time.sleep(3)

# Step 8: Extract and print the first heading text
heading = driver.find_element(By.ID, "firstHeading")
print("Page Heading:", heading.text)

# Step 9: Close the browser
driver.quit()
