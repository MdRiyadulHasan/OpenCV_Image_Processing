import cv2
img= cv2.imread('images\obama.jpg',1)
img=cv2.resize(img, (0,0), fx=.5, fy=.5)
w,h=img.shape[:2]
cx,cy=(w/2,h/2)
angle90=90
angle180=180
angle150=150
angle270=270
scale=.8
# 90 degree anticlockwise
M=cv2.getRotationMatrix2D((cx,cy),angle90, scale)
rotated90 = cv2.warpAffine(img,M,(w,h))
#90 degree clockwise
M=cv2.getRotationMatrix2D((cx,cy),-angle90, scale)
rotated_90_clock = cv2.warpAffine(img,M,(w,h))
#180 clockwise
M=cv2.getRotationMatrix2D((cx,cy),angle180, scale)
rotated_180_clock = cv2.warpAffine(img,M,(w,h))
#150 anticlockwise
M=cv2.getRotationMatrix2D((cx,cy),-angle150, scale)
rotated_150_anti_clock = cv2.warpAffine(img,M,(w,h))
cv2.imshow('original_iamge',img)
cv2.imshow('rotate_90',rotated90)
cv2.imshow('rotated_90_clock',rotated_90_clock)
cv2.imshow('rotated_180_clock',rotated_180_clock)
cv2.imshow('rotated_150_anti_clock',rotated_150_anti_clock)
cv2.waitKey(0)
cv2.destroyAllWindows()
