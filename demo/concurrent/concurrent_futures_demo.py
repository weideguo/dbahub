from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor as PoolExecutor   
#from concurrent.futures import ProcessPoolExecutor as PoolExecutor   # 使用进程实现并发
import time
import random 

max_workers = 3  

def process_task(line):
    """单个任务的执行逻辑"""
    try:
        s = random.random()*5
        time.sleep(s)
        return str(s)+" "+line
    except Exception as e:
        print(f"处理 {line} 失败: {e}")
        return None




results = []

with PoolExecutor(max_workers=max_workers) as executor:
    # 1. 串行读取文件，但只负责提交任务，不等待结果
    # submit 返回一个 Future 对象，代表未来的结果
    future_to_line = {
        executor.submit(process_task, line): line 
        for line in ["aaa","bbb","ccc","ddd","aaa1","bbb1","ccc1","ddd1","aaa2","bbb2","ccc2","ddd2"]
    }
    
    # 2. 遍历完成的任务（as_completed 保证谁先做完谁先返回，不阻塞整体进度）
    for future in as_completed(future_to_line):
        line = future_to_line[future]
        try:
            url = future.result()  # 获取执行结果
            if url:
                print(url)
                results.append(url)
        except Exception as exc:
            print(f"发生异常: {exc}")

