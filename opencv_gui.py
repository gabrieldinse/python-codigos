import numpy as np
import cv2

img = cv2.imread('C:/Users/dell/Desktop/objects.JPG', 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
