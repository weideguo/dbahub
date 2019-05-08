from bs4 import BeautifulSoup
import requests

headers={}

#https://www.baidu.com/s?wd=aaa&pn=16
#https://www.amazon.com/s?k=apple&page=3
html=requests.get("https://www.baidu.com/",headers=headers)


soup = BeautifulSoup(html.text)

titles = soup.select("html > head > title")
titles[0].get_text()

soup.find_all('div')
soup.find_all("a", class_="a-link-normal a-text-normal")
x=soup.find_all("a",id="dp-summary-see-all-reviews")

#查询的结果是BeautifulSoup对象列表
