import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=np.zeros((100,500),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
im=cv2.putText(img1,' VENKATESH E ',(5,70),font,2,(255),5,cv2.LINE_AA)

Kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11))
plt.imshow(im)

image1=cv2.morphologyEx(im,cv2.MORPH_OPEN,Kernel)
plt.imshow(image1)

image1=cv2.morphologyEx(im,cv2.MORPH_CLOSE,Kernel)
plt.imshow(image1)