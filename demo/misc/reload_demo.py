#config.py
a="aaaa"


#demo.py
if __name__ == "__main__":
    import time
    from imp import reload
    import config
    while True:
        reload(config)
        print(config.a)
        time.sleep(2)
        
#config.py可以在线更改 无需重新运行demo.py
