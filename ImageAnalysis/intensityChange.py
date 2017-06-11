import cv2
import numpy as np
import matplotlib.pyplot as pt

img = cv2.imread('pic.jpg', -1)
cv2.imshow("Black and white image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

a,b,c = map(lambda x:x,list(np.shape(img)))

for i in range(a):
    for j in range(b):
        if img[i][j][1]+5 < 255:
            img[i][j][1] += 10
        else:
            img[i][j][1] = 255
        
cv2.imshow("Black and white image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
