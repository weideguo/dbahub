#coding:utf8
#vedio to image

import cv2

vedio_file="WhatsNewFeature_3DModels.mp4"
vc = cv2.VideoCapture(vedio_file)
c=0
rval=vc.isOpened()


def padding(i,l,p="0"):
    p_num=l-len(str(i))
    x=str(i)
    for i in range(p_num):
        x=p+x
    return x

while rval:
    c = c + 1
    rval, frame = vc.read()
    if rval:
        cv2.imwrite("img/"+ padding(c,4) + ".jpg", frame) 
        cv2.waitKey(1)
    else:
        break
vc.release()


