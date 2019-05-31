#!coding:utf8

#亚马逊

from bs4 import BeautifulSoup
import requests
import threading
from threading import Thread



root_url="https://www.amazon.com"

headers={"referer": "https://www.amazon.com/",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

r=requests.Session()

def get_soup(url):
    #html=requests.get(url,headers=headers,verify=False)
    html=r.get(url,headers=headers,verify=False)
    #print html.text
    soup = BeautifulSoup(html.text,'lxml')
    return soup


lock = threading.Lock()

def get_detail(i):
    global lock 
    try:
        i_name=i.select("span")[0].get_text()
    
        detail_url = root_url+i["href"]
    
        soup2 = get_soup(detail_url)
        x = soup2.find_all("a",id="dp-summary-see-all-reviews")
        i_review = x[0].select("h2")[0].get_text()
        
        with lock:
            print "%s ||| %s" % (i_name.encode("utf8"),i_review.encode("utf8"))
        
    except:
        with lock:
            print "ERROR at: %s %s" % (i_name,detail_url)


def main(page,keyword):
    soup=get_soup("https://www.amazon.com/s?k="+keyword+"&page="+str(page))
    item_list = soup.find_all("a", class_="a-link-normal a-text-normal")
    
    ts=[]
    for i in item_list:
        t=Thread(target=get_detail,args=(i,))
        ts.append(t)
    
    for t in ts:
        t.start()
    
    for t in ts:
        t.join()


if __name__=="__main__":
    page_num=5
    keyword="apple"

    for page in range(page_num):
        main(page,keyword)    



