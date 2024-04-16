"""
类似于 selenium

# 安装
pip3 install playwright
playwright install
"""


# 异步
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://www.baidu.com")
        print(await page.title())
        await browser.close()

asyncio.run(main())



# 同步
from playwright.sync_api import sync_playwright

# p = sync_playwright().start()
with sync_playwright() as p:
	# pixel_2 = playwright.devices['Pixel 2']  # Pixel 2 一款安卓手机
	#proxy_ip = {
    #        'server': 'http://',
    #        'username': '',
    #        'password': '',
    #    }
    proxy_ip = None
    # headless：是否无头；slow_mo放慢执行速度
    browser = p.chromium.launch(headless=False, slow_mo=100, proxy=proxy_ip)
	context = browser.new_context(
            viewport={'width': 1800, 'height': 800},	                # 窗口大小
            locale='zh-CN',                                             # 语言zh-CN/en-EN
            timezone_id='Asia/Shanghai',                                # 时区
            color_scheme='dark',	                                    # 颜色
            geolocation={"longitude": 48.858455, "latitude": 2.294474}, # 地理位置
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', # user_agent
            # **pixel_2
        )
	
    
    page = browser.new_page()
    page.goto('http://www.baidu.com')
    print(page.title)
    browser.close()
    
    
    
    