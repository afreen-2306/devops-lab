from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    wait = WebDriverWait(driver, 10)

    heading = wait.until(
        EC.presence_of_element_located((By.ID, "heading"))
    )

    print("Heading:", heading.text)

    name = wait.until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    name.send_keys("Test User")

    email = driver.find_element(By.ID, "email")
    email.send_keys("test@example.com")

    event = driver.find_element(By.ID, "event")
    event.click()

    print("Selenium test passed!")

finally:
    driver.quit()