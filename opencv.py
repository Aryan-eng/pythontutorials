import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('photos/aryan.jpeg')
plt.imshow("Aryan", img)
cv.waitKey(0)