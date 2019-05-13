import cv2
img=cv2.imread('baby.jpg' , cv2.IMREAD_GRAYSCALE)
cv2.imshow('win' , img)
cv2.waitKey(0)
cv2.imwrite('newbaby.jpg' , img)
cv2.destroyAllWindows()
