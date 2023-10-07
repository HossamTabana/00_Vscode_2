from selenium import webdriver
import requests
import pandas as pd
import json

BASE_URL = "https://idatafast.net/apptest"
LOGIN_URL = f"{BASE_URL}/login"
DATA_URL = f"{BASE_URL}/get_website_data"

def authenticate_with_google():
    # Open the login page
    browser = webdriver.Safari()  # Adjust this line if you're using a different browser
    browser.get(LOGIN_URL)
    
    # Wait for manual login
    input("Press Enter after you have logged in manually.")
    
    # Now continue with the rest of your code
    cookies = browser.get_cookies()
    cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
    
    browser.quit()  # Close the browser window
    
    return cookie_dict

def get_data(cookies):
    response = requests.get(DATA_URL, cookies=cookies)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return pd.DataFrame(json_data)
    else:
        raise Exception("Unable to fetch data.")

if __name__ == "__main__":
    # Perform authentication and return cookies
    cookies = authenticate_with_google()
    
    # Fetch the data using the cookies
    data = get_data(cookies)
    print(data)
