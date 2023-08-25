'''
不能放后台运行，会出现获取窗口失败
因此不能在计划任务中设置“不管用户是否登录都要运行”
'''
import time
import os

import win32clipboard
import win32con
import win32api
import win32gui


f=open("x.log", "a")
f.write(str(time.time())+"\n")
def print(s):
    f.write(str(s)+"\n")

def set_paste_text(paste_text):
    """把文字放入剪贴板"""
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,paste_text)   #设置粘贴板为字符串
    win32clipboard.CloseClipboard()
    
    #number=[1,2,3,4,5,6,7,8]
    #bytes([number])
    #win32clipboard.SetClipboardData(win32con.CF_BINARY, data)
    

def ctrl_v():
    """ctrl+v"""
    win32api.keybd_event(17,0,0,0)                        #按下ctrl
    win32api.keybd_event(86,0,0,0)                        #按下V
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放V
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) #释放ctrl
    

def alt_s():
    """alt+s"""
    win32api.keybd_event(18,0,0,0)
    win32api.keybd_event(83,0,0,0)
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
    

def enter():
    """回车键"""
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        

def click():
    """鼠标单击"""
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    

def cursor_move_pos(x,y):
    """移动光标到的位置"""
    win32api.SetCursorPos((x,y))


def get_all_windows():
    """获取所有的窗口"""
    # handler classname title
    all_windows = {}
    
    def enum_windows(hwnd, arg):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            all_windows.update({hwnd: [win32gui.GetClassName(hwnd), win32gui.GetWindowText(hwnd)]})    
    
    win32gui.EnumWindows(enum_windows, 0)
    return all_windows
    

def get_handlers(title):
    """
    根据标题获取对应窗口的句柄
    hwnd=win32gui.FindWindow("WeChatMainWndForPC", '微信') 这种也可以获取句柄，但有些窗口有多个，通过这种获取则不正确
    """
    all_windows = get_all_windows()
    handlers = []
    for h,(class_name, _title) in all_windows.items():
        if _title == title:
            handlers.append(h)
    handlers.sort()
    return handlers
 

if __name__=="__main__":
    #app_path="C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"
    #os.startfile(app_path)
    
    send_content="把这条消息当成测试从而不理会"                # 这里是需要发送的信息内容
    
    #hwnd=win32gui.FindWindow(None, '微信')     
    hwnd=win32gui.FindWindow("WeChatMainWndForPC", '微信')     # 返回微信窗口的句柄信息
    if not hwnd:
        print("获取窗口失败，请检查代码")
        time.sleep(3)
        exit(1)
    
    """
    win32con.SW_HIDE          隐藏窗口。
    win32con.SW_SHOWNORMAL    以正常大小显示窗口。
    win32con.SW_SHOWMINIMIZED 将窗口最小化。
    win32con.SW_SHOWMAXIMIZED 将窗口最大化。
    win32con.SW_SHOW          显示窗口，并保持其大小。
    """
    # 设置窗口位于最上层
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)          # 显示窗口
    time.sleep(1)
    win32gui.MoveWindow(hwnd,0,0,700,500,True)                 # 将窗口移动到指定位置和并设置大小
    time.sleep(1)
    # 根据具体位置移动光标
    cursor_move_pos(200,90)      #单击群
    click()
    
    cursor_move_pos(500,400)     #单击群的对话框
    click()
    
    time.sleep(1)      
    set_paste_text(send_content)
    ctrl_v()
    #enter()
    
    alt_s()
    print("send done")
    time.sleep(1)   #使用sleep是必须的
    # 关闭窗口
    #win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    time.sleep(3)


    # 设置窗口位于最上层
    #win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
