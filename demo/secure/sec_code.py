import base64
base64.b64encode('__import__')

'X19pbXBvcnRfXw=='.decode('base64')


def make_secure():
    """
    移除模块
    """
    UNSAFE = ['open',
              'file',
              'execfile',
              'compile',
              'reload',
              '__import__',
              'eval',
              'input']
    for func in UNSAFE:
        try:
            del __builtins__.__dict__[func]
        except:
            pass



#通过特殊方式引入file模块
__builtins__.__dict__['file']=().__class__.__bases__[0].__subclasses__()[40]


