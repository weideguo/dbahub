
from PIL import Image,ImageDraw

img=Image.open('1.jpg')

# 截取
c_left=    100
c_top=     100
c_right=   100
c_bottom=  100

# 原图片截取成正方形
img_crop=img.crop((c_left,c_top,c_right,c_bottom))


######################################################
"""
jpg失真压缩
PNG无损数据压缩

R 红
G 绿
B 蓝
A Alpha透明度
"""


from PIL import Image, ImageDraw


# 背景
bg_size = (100, 100)    #像素px
bg_color = (0,255,0)
bg = Image.new('RGB', bg_size, color=bg_color)

# 透明背景
#bg_color = (0,0,0,0)
#bg = Image.new('RGBA', bg_size, color=bg_color)

# 
avatar_size = (100, 100)
avatar = Image.open('1.jpg')


# 新建一个蒙板图，必须是 RGBA 模式
# 在此画一个圆
mask = Image.new('RGBA', avatar_size, color=(0,0,0,0))
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0,0, avatar_size[0], avatar_size[1]), fill=(0,0,0,255))


x, y = int((bg_size[0]-avatar_size[0])/2), int((bg_size[1]-avatar_size[1])/2)
box = (x, y, (x + avatar_size[0]), (y + avatar_size[1]))

# box 为图片在 bg 中的位置
# mask 为蒙板，原理同 ps， 只显示 mask 中 Alpha 通道值大于等于1的部分
bg.paste(avatar, box, mask)

bg.save("_1.jpg")

# bg.show()   # GUI环境
