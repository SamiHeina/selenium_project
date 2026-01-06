import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") 
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(5)

    yield driver

    print("Demo complete! Browser will close in 5 seconds...")
    time.sleep(5)

    driver.quit()



