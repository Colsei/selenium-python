from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:/The REST/Career/Automation Test/Eclipse_Java/04 - Windows Software/chromedriver-win64/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.google.com")

print(driver.title)
print(driver.current_url)

driver.maximize_window()
driver.get("https://drive.google.com/drive/u/0/home")
driver.back()
driver.refresh()
driver.forward()

driver.close()