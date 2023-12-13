from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:/The REST/Career/Automation Test/Eclipse_Java/04 - Windows Software/chromedriver-win64/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)

url = "https://rahulshettyacademy.com/angularpractice"

driver.get(url)

# //svg[@class='ic ic-hamger']
#element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
#)
#element.click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

input("Nhấn Enter để đóng trình duyệt")
driver.quit()