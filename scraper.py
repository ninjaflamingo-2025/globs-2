import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')  # This will run the browser in the background without a UI
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)
driver.get("https://www.example.com")
