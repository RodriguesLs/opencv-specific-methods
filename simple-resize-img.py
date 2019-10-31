import cv2
import numpy as np

img = cv2.imread('/home/pi/Pictures/peoples.jpeg')
cv2.imshow('Original', img)
width= img.shape[1]
height = img.shape[0]
proportion = float(height/width)
new_width = 320 #pixels
new_height = int(new_width*proportion)
new_size = (new_width, new_height)

img_resized = cv2.resize(img, new_size, interpolation = cv2.INTER_AREA)

cv2.imshow('Result', img_resized)
cv2.waitKey(0)
