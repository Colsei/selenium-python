from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://tinhte.vn/forums/xe-hoi.545/"
driver.get(url)

elements = driver.find_element(By.CSS_SELECTOR,"a.PreviewTooltip")

for i in range(min(10, len(elements))):
    title = elements[i].text.strip()
    print("Title {}: {}".format(i + 1, title))

driver.quit()