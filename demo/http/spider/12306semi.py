#coding:utf8
"""
半自动抢票
需要手动点击验证图片与提交登陆
"""
username="123456@a.com"
passwd="123456789"

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

url="https://kyfw.12306.cn/otn/resources/login.html"

driver = webdriver.Chrome() 
driver.get(url)


b=driver.find_element_by_class_name("login-hd-account")
b.click()


i=driver.find_element_by_id("J-userName")
i.send_keys(username)


i=driver.find_element_by_id("J-password")
i.send_keys(passwd)



b=driver.find_element_by_class_name("login-btnlo")
b.click()

try:
    #存在全局提示框 则关闭
    b=driver.find_element_by_class_name("modal-close")
    if b:
        b.click()
except:
    pass

#首页
i=driver.find_element_by_id("J-chepiao")
action = ActionChains(driver)
action.move_to_element(i).perform()
    
#进入单程选票页面
b=driver.find_element_by_name("g_href") 
b.click()   
   


from selenium.webdriver.common.keys import Keys

#输入地址
i=driver.find_element_by_id("fromStationText") 
i.send_keys(Keys.ENTER)
#防止输入框已经存在字符
for ii in range(10):  
    i.send_keys(Keys.BACK_SPACE)  
i.send_keys("gz")  
i.send_keys(Keys.ENTER)  


i=driver.find_element_by_id("toStationText") 
i.send_keys(Keys.ENTER)
#防止输入框已经存在字符
for ii in range(10):  
    i.send_keys(Keys.BACK_SPACE)  
i.send_keys("nanning")  
i.send_keys(Keys.ENTER)  

"""
h1 = dr.current_window_handle
 
＃点击网页某一元素，点击后浏览器会弹出另一个窗口 
dr.find_element_by_id("你要点击的元素").click() 
＃获取所有的句柄，是个list 
all_h = dr.window_handles 
＃跳转到第二个窗口 
dr.switch_to.window(all_h[1])

"""


###########################以上作废

#https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%B9%BF%E5%B7%9E%E5%8D%97,IZQ&ts=%E5%8D%97%E5%AE%81,NNZ&date=2020-05-01&flag=N,N,Y


#路径可以在查询时确定
url="https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=广州南,IZQ&ts=南宁,NNZ&date=2020-05-01&flag=N,N,Y"

"""
使用场景为已经登陆好 自动抢票
如果发生登出，登陆后继续自动自动抢票
"""

username="123456@a.com"
passwd="123456789"
#获取可选择的按钮队列
bs=driver.find_elements_by_class_name("btn72")

while True
    i=0
    for b in bs:

        #发车时间
        attr=b.get_attribute("onclick")
        h,m=attr.split(",")[-4].replace("'","").split(":")
        h=int(h)
        if match(h,i):
            b.click()
            break

       
def match(h,i=0):
    #优先级别
    q=[(10,13),(13,15),(15,17),(9,10),(8,9),(6,7)]        
    if i>=len(q):
        return True
    else:
        if h>=q[i](0) and h<=q[i](1):
            return True
        else:
            return False
        
"""
onclick="checkG1234('OSNPIUyCf0G4','IZQ','NFZ')"


"""
#可能出现登陆验证
try:
    #存在全局提示框 则关闭
    b=driver.find_element_by_class_name("modal-login-tit")
    if b:
        b=driver.find_element_by_class_name("login-hd-account")
        b.click()
        
        
        i=driver.find_element_by_id("J-userName")
        i.send_keys(Keys.ENTER)
        #防止输入框已经存在字符
        for ii in range(50):  
            i.send_keys(Keys.BACK_SPACE) 
        i.send_keys(username)
        
        
        i=driver.find_element_by_id("J-password")
        i.send_keys(passwd)
        
     while True:
        #登陆框一直存在，则一直等待
        try:
            b=driver.find_element_by_class_name("modal-login-tit")
            time.sleep(1)
        except:
            break
        
     
except:
    pass