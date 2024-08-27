from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setting up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://www.saucedemo.com/')

# Get the page source (HTML content)
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')
page_text = soup.get_text()

# Save the content to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_text)

print("Webpage content saved to Webpage_task_11.txt")