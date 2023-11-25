from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def login():
    options = webdriver.FirefoxOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get("#webpage#")

        username = "USERNAME"
        password = "PASSWORD"

        wait = WebDriverWait(driver, 20)

        # Wait for the username input field to be visible and clear it before typing
        username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[name="login"] input[name="username"]')))
        username_input.clear()
        username_input.send_keys(username)

        # Wait for the password input field to be visible and clear it before typing
        password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[name="login"] input[name="password"]')))
        password_input.clear()
        password_input.send_keys(password)

        # Find and click the login button
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[name="login"] input[type="submit"]')))
        submit_button.click()

        print("Logged in successfully")

    finally:
        # Close the browser, even if there's an exception
        driver.quit()

def perform_login():
    while True:
        login()
        # Wait for some time before attempting to log in again (e.g., 6 hours)
        time.sleep(6 * 60 * 60)

# Call perform_login initially to start the process
perform_login()
