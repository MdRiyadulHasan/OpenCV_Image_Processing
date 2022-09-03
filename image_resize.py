import cv2
img1= cv2.imread('images\obama.jpg',1)
img2=cv2.resize(img1,(400,400))
cv2.imshow('original_image',img1)
cv2.imshow('resized_image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
