import numpy as np
import cv2
from scipy import ndimage

img = cv2.imread('stars.jpg',0)
cv2.imshow("Black and white image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


a,b = map(lambda x:x,list(np.shape(img)))

for i in range(a):
    for j in range(b):
        if img[i][j] < 200:
            img[i][j] = 0


cv2.imshow("Converted image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



img = cv2.GaussianBlur(img, (5,5), 0)
maxValue = 255
adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType = cv2.THRESH_BINARY
blockSize = 5
C = -3
im_thresholded = cv2.adaptiveThreshold(img, maxValue, adaptiveMethod, thresholdType, blockSize, C) 
labelarray, particle_count = ndimage.measurements.label(im_thresholded)

print(particle_count)