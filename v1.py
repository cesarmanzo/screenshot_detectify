from selenium import webdriver
import time
import sys

br = webdriver.ChromeOptions()
br.add_argument('headless')
br.add_argument('hide-scrollbars')
br.add_argument('kiosk')
driver = webdriver.Chrome(chrome_options=br)
driver.get('https://saam.digital')
height = driver.execute_script(
    """return Math.max(document.body.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.clientHeight,
        document.documentElement.scrollHeight,
        document.documentElement.offsetHeight)""")

print(height)
driver.set_window_size(1366, height)
title = driver.title
time.sleep(2)
driver.get_screenshot_as_file('XXXXX.png')
driver.quit
print('END', title)
