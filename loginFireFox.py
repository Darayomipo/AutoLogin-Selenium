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
        driver.get("ADDRESS")

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
    wait_time = 6 * 60 * 60  # 6 hours in seconds

    while True:
        start_time = time.time()
        login()
        elapsed_time = time.time() - start_time
        print(f"Login attempt took {elapsed_time:.2f} seconds")

        remaining_time = wait_time
        while remaining_time > 0:
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"Time until next login: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds", end="\r")
            time.sleep(1)
            remaining_time -= 1


perform_login()
