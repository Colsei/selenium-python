from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#Case 1: Registration-Sign-in
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

#driver.find_element(By.CSS_SELECTOR,"a[href='https://practice.automationtesting.in/my-account/']").click() -> cần thời gian chờ Element xuất hiện.

my_account = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']"))
)
my_account.click()
driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']").send_keys('vuhu1h@yopmail.com')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']").send_keys('@!Adssdf32a123456')

#driver.find_element(By.NAME, "register").click() -> pw quá yếu có thể nút Register k enabled để click chuẩn.
register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='woocommerce-Button button'][value='Register']"))
)
register_button.click()

driver.find_element(By.CSS_SELECTOR, "img[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/color-logo-original.png']").click()
time.sleep(3)

driver.quit()
print("Case 1 passed.")
print(" ")



#Case 2: Registration with invalid Email-id
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

my_account = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']"))
)
my_account.click()
driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']").send_keys('vuhuyhuuyopmailcom')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']").send_keys('@!Adssdf32a123456')

register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='woocommerce-Button button'][value='Register']"))
)
register_button.click()

popup_error = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "woocommerce-error"))
)
print("Error text:", popup_error.text)

driver.quit()
print("Case 2 passed.")
print(" ")



#Case 3: Registration with empty Email-id
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

my_account = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']"))
)
my_account.click()
driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']").send_keys('@!Adssdf32a123456')

register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='woocommerce-Button button'][value='Register']"))
)
register_button.click()

error_message_3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//li/strong[text()='Error:']/following-sibling::text()"))
)
print("Error text:", error_message_3.text)

driver.quit()
print("Case 3 passed.")
print(" ")



#Case 4: Registration with empty password
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

my_account = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']"))
)
my_account.click()
driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']").send_keys('vhh@yopmail.com')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']").click()

register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='woocommerce-Button button'][value='Register']"))
)
register_button.click()

error_message_4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//li/strong[text()='Error:']/following-sibling::text()"))
)
print("Error text:", error_message_4.text)

driver.quit()
print("Case 4 passed.")
print(" ")



#Case 5: Registration with empty Email-id & password
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

my_account = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']"))
)
my_account.click()
driver.find_element(By.CSS_SELECTOR, "input[id='reg_email']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id='reg_password']").click()

register_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='woocommerce-Button button'][value='Register']"))
)
register_button.click()

error_message_5 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//li/strong[text()='Error:']/following-sibling::text()"))
)
print("Error text:", error_message_5.text)

driver.quit()
print("Case 5 passed.")
print(" ")