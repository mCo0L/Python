import numpy as np
import cv2

img = cv2.imread('stars.jpg',0)
print(img)
a,b = map(lambda x:x,list(np.shape(img)))
print(a,b)
for i in range(a):
    for j in range(b):
        if img[i][j] < 200:
            img[i][j] = 0
print(img)
cv2.imshow("Image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()