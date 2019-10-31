import cv2

img = cv2.imread('/home/pi/Pictures/young.jpeg')
slice = img[100:200, 100:200]
cv2.imshow('Image sliced: ', slice)
cv2.imwrite('output/crop-img.jpeg', slice)

cv2.waitKey(0)
