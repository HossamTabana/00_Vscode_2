import requests
import pandas as pd
from selenium import webdriver

BASE_URL = "https://idatafast.net/apptest"
LOGIN_URL = f"{BASE_URL}/login"
DATA_URL = f"{BASE_URL}/get_website_data"

def authenticate_with_google():
    # Note: This requires manual intervention unless automated using Selenium or another tool
    browser = webdriver.Safari()
    browser.get(LOGIN_URL)
    
    # You will need to add steps here to automate the login process using Selenium.
    # This can be tricky since Google might detect and block automated login attempts.
    
    # After login is complete and you're redirected, you should have a session with the access token.
    cookies = browser.get_cookies()
    browser.close()
    return {cookie['name']: cookie['value'] for cookie in cookies}

def get_data(cookies):
    response = requests.get(DATA_URL, cookies=cookies)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise ValueError("Unable to fetch data")

if __name__ == "__main__":
    cookies = authenticate_with_google()
    data = get_data(cookies)
    print(data)

