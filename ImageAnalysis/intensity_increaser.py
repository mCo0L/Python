import numpy as np
import cv2

img=cv2.imread('flower.jpg',-1)
print(img)

for i in img:
    for ii in i:
        if(ii[0]<50 and (ii[1]>150 or ii[2]>150)):
            ii[0]=255
        
cv2.imshow('img',img)
cv2.waitKey(0)

