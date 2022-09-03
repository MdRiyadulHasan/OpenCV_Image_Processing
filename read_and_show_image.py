import cv2
img1=cv2.imread('images\messi.jpg', 0)     #cv2.IMREAD_GRAYSCALE
img2=cv2.imread('images\messi.jpg', 1)    #cv2.IMREAD_UNCHANGED
img3=cv2.imread('images\messi.jpg', -1)    #cv2.IMREAD_COLOR
cv2.imshow('Showing_grayscale', img1)
cv2.imshow('Original_Image', img2)
cv2.imshow('Color_Image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/messi_grayscale.jpg',img1)
