from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Initialize WebDriver (using Chrome here)
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Step 3: Find the search box
search_box = driver.find_element(By.NAME, "q")

# Step 4: Type a query into the search box
search_box.send_keys("Selenium Python tutorial")

# Step 5: Press ENTER
search_box.send_keys(Keys.RETURN)

# Optional: Wait to see results
time.sleep(5)

# Step 6: Close the browser
driver.quit()
