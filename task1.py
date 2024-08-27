from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setting up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://www.saucedemo.com/')

# Fetch the current URL
current_url = driver.current_urlpython 
print("Current URL:", current_url)

# Close the WebDriver
driver.quit()