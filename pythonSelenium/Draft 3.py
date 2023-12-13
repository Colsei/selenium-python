from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

# Mở trang web
urls = [
    "https://tinhte.vn/thread/vinfast-chinh-thuc-mo-coc-vf-7.3747695/",
    "https://tinhte.vn/thread/kia-sportage-hybrid-2024-ra-mat-moi-anh-em-tham.3747958/",
]

# Khởi tạo danh sách để lưu dữ liệu
all_data = {'Tiêu đề': [], 'Nội dung': []}

for url in urls:
    driver.get(url)

    # Lấy tiêu đề bài báo
    title = driver.title

    # Lấy nội dung bài báo
    content_element = driver.find_element(By.CLASS_NAME,"xf-body-paragraph")
    content = content_element.text.strip()

    # In tiêu đề và nội dung ra console (kiểm tra)
    print("Tiêu đề:", title)
    print("Nội dung:", content)

    # Thêm dữ liệu vào danh sách
    all_data['Tiêu đề'].append(title)
    all_data['Nội dung'].append(content)

# Đóng trình duyệt
driver.quit()

# Tạo DataFrame từ dữ liệu
dataframe = pd.DataFrame(all_data)

# Xuất DataFrame ra file Excel
dataframe.to_excel('C:/The REST/Career/Automation Test/PyCharm_Python/Bài tập/Get data from article/tinhte_articles3.xlsx', index=False)