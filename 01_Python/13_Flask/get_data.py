import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://idatafast.net/apptest"
LOGIN_URL = f"{BASE_URL}/login"
DATA_URL = f"{BASE_URL}/get_website_data"

def authenticate_with_google():
    # Initialize the Selenium WebDriver
    browser = webdriver.Safari() # Change this to your preferred driver
    browser.get(LOGIN_URL)
    
    # NOTE: Add code here to automate Google login
    # This is a placeholder. Actual elements and flow can vary!
    email_elem = browser.find_element(By.ID, 'identifierId')
    email_elem.send_keys('hossam.tabana@gmail.com')
    email_elem.send_keys(Keys.RETURN)
    time.sleep(2)
    
    password_elem = browser.find_element(By.NAME, 'password')
    password_elem.send_keys('your-password')
    password_elem.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Give some time for login to complete and to manually complete any CAPTCHAs or 2FA
    
    # After login is complete and you're redirected, you should have a session with the access token.
    cookies = browser.get_cookies()
    browser.quit()
    return {cookie['name']: cookie['value'] for cookie in cookies}

def get_data(cookies):
    response = requests.get(DATA_URL, cookies=cookies)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise ValueError("Unable to fetch data")

if __name__ == "__main__":
    cookies = authenticate_with_google()
    print(f"Cookies: {cookies}")
    
    if cookies:
        data = get_data(cookies)
        print(data)
    else:
        print("Failed to authenticate.")
