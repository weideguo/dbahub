#!/bin/env python
#coding:utf8

"""
使用浏览器模拟运行http请求与操作
chrome 需要安装ChromeDriver
将解压后的文件放入配置了环境变量的文件夹，或者新设置环境变量

#其他浏览器需要下对应的驱动

https://www.selenium.dev/selenium/docs/api/py/
"""

#直接打开浏览器图形界面
from selenium import webdriver

#driver = webdriver.Firefox()  
driver = webdriver.Chrome()     

url="'https://www.baidu.com'"
#driver可以随鼠标操作后动态改变
driver.get(url)     
driver.quit()         


###########################################################
#无界面运行，chrome>=58
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_opt = Options()                                   
chrome_opt.add_argument('--headless')                    # 无界面化
chrome_opt.add_argument('--disable-gpu')                 # 配合上面的无界面化
chrome_opt.add_argument('--window-size=1366,768')        # 设置窗口大小，窗口大小会有影响

#driver = webdriver.Chrome(chrome_options=chrome_opt)        
driver = webdriver.Chrome(options=chrome_opt)  
driver.get(url)       

print(driver.page_source)                 #访问获取到的源码
driver.save_screenshot("screen.png")      #源码渲染成图片并保存
driver.quit()   



"""
url="https://passport.jd.com/new/login.aspx"
20200411
"""

#获取按钮并点击
b=driver.find_element_by_class_name('login-tab-r')
b.click()

#获取输入框并输入
i=driver.find_element_by_id('loginname')
i.send_keys('11111')

i=driver.find_element_by_id('nloginpwd')
i.send_keys('2222')


b=driver.find_element_by_id('loginsubmit')
b.click()



from selenium.webdriver.common.action_chains import ActionChains

#拖拽滑块
dragger=driver.find_element_by_class_name('JDJRV-slide-btn')
action = ActionChains(driver)
action.drag_and_drop_by_offset(dragger, 85, 0).perform()


#获取截图对象
screenshot=driver.get_screenshot_as_png()
f=open('screenshot.png','wb+')
f.write(screenshot)
f.seek(0)    


#获取图片
img=driver.find_element_by_class_name('JDJRV-bigimg')
location=img.location
size=img.size

img=driver.find_element_by_class_name('JDJRV-smallimg')
location=img.location
size=img.size

left = int(location['x'])
top = int(location['y'])
right = left + int(size['width'])
bottom = top + int(size['height'])

from PIL import Image

screenshot = Image.open(f)
#截取图片
c=screenshot.crop((left, top, right, bottom))



#移动鼠标
element = driver.find_element_by_class_name('login-tab-l')
action = ActionChains(driver)
action.move_to_element(element).perform()



