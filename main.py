from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置Chrome浏览器选项
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r'C:\\Program Files\\Google\\Chrome\Application\\chrome.exe' 
# 指定Chrome浏览器路径

# 创建Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 打开指定网站
driver.get('https://finder.swu-nlp.cn/#/chat')

# 等待页面加载完成，最多等待30秒
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="账号"]')))

# 在页面加载完毕后，执行后续操作
account_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="账号"]')
account_input.send_keys("your_account") 
# 将您的账号替换为实际账号
password_input = driver.find_element("id", "password")
password_input.send_keys("your_password") 
# 将您的密码替换为实际密码

# 定位复选框的外围元素并点击
switch_core = driver.find_element(By.CSS_SELECTOR, '.el-switch__core')
switch_core.click()

login_button = driver.find_element(By.ID, "loginBtn")
driver.execute_script("arguments[0].click();", login_button)

# 打开文本文件
with open(r"C:\\Users\\lin\Desktop\\ask5.txt", 'r', encoding = "utf-8") as file:
    for line in file:
        line = line.strip()

        # 添加额外的等待，确保页面已经加载完成
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'el-input__inner')))

        # 定位输入框并输入文本
        input_box = driver.find_element(By.CLASS_NAME, 'el-input__inner')
        input_box.clear()
        input_box.send_keys(line)

        # 等待确认按钮变为可点击状态并点击
        confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "realBtn")))
        confirm_button.click()

        # 等待一定时间以确保操作完成
        time.sleep(30)  # 示例：等待30秒

time.sleep(5)
driver.quit()
