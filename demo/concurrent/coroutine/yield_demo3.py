import time

# 生产者
def product():
    data =0
    while True:
        data = data+1
        print("product %s" % data)         # 需要消费触发才执行
        if data:
            yield data
        else:
            break

# 消费者
for x in  product():
    time.sleep(0.1)
    print("consume %s" % x)
    time.sleep(3)
    