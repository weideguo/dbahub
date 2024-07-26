#url编码与解码

#python3
import urllib.parse

en_url = urllib.parse.quote("hello 世界!")

de_url = urllib.parse.unquote(en_url)


#python 2
import urllib
urllib.quote("@#$@#")

