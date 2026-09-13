from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Open the HTML file
driver.get("file:///C:/Users/afree/OneDrive/Desktop/selenium_test/index.html")

# Maximize browser
driver.maximize_window()

# Verify heading
heading = driver.find_element(By.ID, "heading")

if heading.text == "Welcome to Selenium Testing":
    print("TEST 1 PASSED: Page heading is correct")
else:
    print("TEST 1 FAILED")

# Enter name
name_box = driver.find_element(By.ID, "name")
name_box.send_keys("Naga Mani")

# Click button
button = driver.find_element(By.ID, "btn")
button.click()

time.sleep(2)

# Verify result
message = driver.find_element(By.ID, "message")

if message.text == "Hello, Naga Mani!":
    print("TEST 2 PASSED: Greeting is correct")
else:
    print("TEST 2 FAILED")

# Close browser
driver.quit()
