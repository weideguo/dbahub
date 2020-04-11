#coding:utf8
#图像处理
from PIL import Image

#通过文件名、文件对象打开
im = Image.open('test.jpg')
w, h = im.size

#图像缩放
im.thumbnail((w//2, h//2))

from PIL import Image, ImageFilter

#模糊
im = im.filter(ImageFilter.BLUR)
im.save('new.jpg', 'jpeg')




#创建图片
width, height = 200,100
r,g,b=0,0,0
image = Image.new('RGB', (width, height), (r,g,b))

#描绘
draw = ImageDraw.Draw(image)

#描绘点
x, y = 100,50
r,g,b= 255,255,255
draw.point((x, y), fill=(r,g,b))

#描绘文字
x,y=70, 10
c="A"
r,g,b=255,255,255
#字体
#centos /usr/share/fonts
#windows c:/Windows/Fonts
font = ImageFont.truetype('FreeMonoBold.ttf',36) 
draw.text((x,y), c, font=font, fill=(r,g,b))

image.save("aaa.png")

