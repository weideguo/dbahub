# python字符串的前缀

# 默认\会被转义处理
s = "x\a\b"
# 需要额外加\防止转义
s = "x\\a\\b"

# 原始字符串(Raw string),禁用转义字符处理
s = r"x\a\b"

# 格式化字符串(f-strings)
name = 111
s = f"Hello {name}"

# 字节字符串(Bytes)
#s = b"中文"                        # python2
s = b'\xe4\xb8\xad\xe6\x96\x87'

# Unicode 字符串
s = u"中文"
