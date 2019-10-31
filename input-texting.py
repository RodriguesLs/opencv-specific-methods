import cv2
import numpy as np

img = cv2.imread('/home/pi/Pictures/peoples.jpeg')
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'Rodrigues OpenCV', (15,65), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('First text input', img)
cv2.imwrite('output/img-text.jpeg', img)
cv2.waitKey(0)
