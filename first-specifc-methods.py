#import opencv and numpy (with alias)
import cv2
import numpy as np

#Declaring variables
origin_img = '/home/pi/Pictures/young.jpeg'
output_img = 'output/first-output.jpg'

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

img = cv2.imread(origin_img)

#Using opencv methods
cv2.line(img, (0, 0), (100, 200), green)
cv2.line(img, (300, 200), (150, 150), red, 5)
cv2.rectangle(img, (20, 20), (120, 120), blue, 10)
cv2.rectangle(img, (200, 50), (225, 125), green, -1)

(x, y) = (img.shape[1] // 2, img.shape[0] // 2)

for raio in range(0, 175, 15):
  cv2.circle(img, (x, y), raio, red)

cv2.imshow('Painting on image: ', img)
cv2.imwrite(output_img, img)
cv2.waitKey(0)
