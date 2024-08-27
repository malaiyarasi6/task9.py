from selenium import webdriver

# Set up the WebDriver (make sure you have the correct driver installed, e.g., ChromeDriver)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.saucedemo.com/")

# Fetch the title of the webpage
title = driver.title
print("Title of the webpage:", title)

# Close the WebDriver
driver.quit()