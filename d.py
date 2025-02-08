from selenium import webdriver

# Specify the path to Chrome WebDriver executable
webdriver_path ="'''''' C:\path\to\chromedriver.exe'''''''''"

# Initialize Chrome WebDriver without executable_path
driver = webdriver.Chrome(webdriver_path)

# Open Google's homepage
driver.get("https://www.google.com")
