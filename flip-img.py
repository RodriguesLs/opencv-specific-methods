import cv2

img = cv2.imread('/home/pi/Pictures/young.jpeg')
cv2.imshow('Origin', img)

horizontal_flip = img[::-1, :] #manual method
#horizontal_flip = cv2.flip(img, 1)

cv2.imshow('Horizontal flip', horizontal_flip)

vertical_flip = img[:, ::-1] #manual method
#vertical_flip = cv2.flip(img, 0)

cv2.imshow('Vertical flip', vertical_flip)

hv_flip = img[::-1, ::-1] #manual method
#hv_flip = cv2.flip(img, -1)
cv2.imshow('Horizontal and Vertical flip', hv_flip)
cv2.waitKey(0)
