import cv2
img = cv2.imread('/home/pi/Pictures/young.jpeg')

(h, w) = img.shape[:2] #get height and width
center = (w //2, h //2) #get center of image

M = cv2.getRotationMatrix2D(center, 30, 1.0) #30 degrees
img_rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow('Rotated image', img_rotated)
cv2.waitKey(0)
