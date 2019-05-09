import requests
from contextlib import closing
 
def download(url,filename):
    with closing(requests.get(url, stream=True)) as response:
        chunk_size = 1024                                                       # 单次请求最大值
        content_size = int(response.headers['content-length'])                  # 内容体总大小
        data_count = 0
        with open(filename, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_count = data_count + len(data)
                yield data_count,content_size
                

if __name__ == '__main__':
    url = 'https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.16-winx64.zip'
    filename="my_download_file"
    
    for data_count,content_size in download(url,filename):
        now_jd = data_count * 100 / content_size
        print("\r %d%%(%d/%d) - %s" % (now_jd, data_count, content_size, url),end=" ")    #only work on python3
        #print now_jd, data_count, content_size, url
