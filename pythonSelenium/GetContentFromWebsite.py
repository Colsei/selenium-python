from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

# Mở trang web
url = "https://tinhte.vn/thread/new-mazda-cx-3-2024-ra-mat-tai-viet-nam-nang-cap-trang-bi-gia-tu-524-trieu-dong.3745833/"
driver.get(url)

# Lấy tiêu đề bài báo
title_element = driver.find_element(By.CSS_SELECTOR,"h1.jsx-89440")
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
title = title_element.text.strip()

# Lấy nội dung bài báo
content_element = driver.find_element(By.CSS_SELECTOR,"article.jsx-89440 div.jsx-89440")
content = content_element.text.strip()

# Đóng trình duyệt
driver.quit()

# In tiêu đề và nội dung ra console (kiểm tra)
print("Tiêu đề:", title)
print("Nội dung:", content)

# Tạo DataFrame từ dữ liệu
data = {'Tiêu đề': [title], 'Nội dung': [content]}
dataframe = pd.DataFrame(data)

# Xuất DataFrame ra file Excel
dataframe.to_excel('C:/The REST/Career/Automation Test/PyCharm_Python/Bài tập/Get data from article/tinhte_article1.xlsx', index=False)