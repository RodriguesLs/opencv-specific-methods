import cv2

img = cv2.imread('/home/pi/Pictures/young.jpeg')
cv2.imshow('Original', img)
img_resized = img[::3,::3]

cv2.imshow('Image resized', img_resized)
cv2.waitKey(0)


