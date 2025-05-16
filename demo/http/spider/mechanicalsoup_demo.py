import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

# 登录网站
browser.open("https://www.example.com/login")
browser.select_form('form[action="/login"]')
browser["username"] = "user123"
browser["password"] = "pass123"
response = browser.submit_selected()

# 访问登录后的页面
browser.open("https://www.example.com/dashboard")
print(browser.get_current_page().title.text)

