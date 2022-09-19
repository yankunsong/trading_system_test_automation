from selenium import webdriver

options = webdriver.ChromeOptions()
# 设置窗口大小
options.add_argument('window-size=1920x1080')
# 去除浏览器正在受到自动测试软件的控制
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 解决无法访问https的问题
options.add_argument('--ignore-certificate-errors')
# 允许忽略TLS/SSL错误
options.add_argument('--allow-insucre-localhost')
# 无痕模式
options.add_argument('--incognito')
# 设置为无头模式，不打开浏览器
options.add_argument('--headless')
# 解决卡顿
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')