# 进度条

from tqdm import tqdm
import time
 
def f1():
    # 总进度100
    pbar = tqdm(total=100) 
    
    # 总共更新10次
    for i in range(10):
        time.sleep(0.2)
        
        # 每次更新进度10
        pbar.update(10)
    
    pbar.close()



def f2():
    data = range(100)
    
    for item in tqdm(data):
        time.sleep(0.01)


if __name__ == "__main__":
    #f1()
    f2()
