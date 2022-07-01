from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union

"""
https://legacy.python.org/dev/peps/pep-0484/
python3.5 引入类型注释
并没有实现强制参数传入，参数以旧可以以动态类型传入，只是利于文档生成以及编辑器使用
"""


def greeting(name: str) -> str:
    return 'Hello ' + name
    
    


