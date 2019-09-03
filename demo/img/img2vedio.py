#coding:utf8
#img to vedio


import cv2
import glob
 
fps = 60                           #帧率 Frames Per Second
vedio_filename="saveVideo.avi" 
img_size=(220,220)
img_files="img/*.jpg"

#压缩格式
#如果不行先装ffmepg？: yum install ffmepg 
#可以用(*"DVIX") (*"X264") (*"MJPG")   #即('M','J','P','G')
fourcc = cv2.VideoWriter_fourcc(*"MJPG")   
videoWriter = cv2.VideoWriter(vedio_filename, fourcc, fps, img_size)

#获取符合的路径 路径的排序格式需要预先设置好
imgs=glob.glob(img_files)     
for imgname in imgs:
    frame = cv2.imread(imgname)
    videoWriter.write(frame)

videoWriter.release()
