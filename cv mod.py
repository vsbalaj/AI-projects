import cv2

image=cv2.imread("tesimg.jpg")

grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('show',image)
cv2.imshow('gray',grayimg)

##cv2.imwrite('photo.jpg',image)
##
cv2.waitKey(5000)
##
cv2.destroyAllWindows()

print(image.shape)
print(image.size)
