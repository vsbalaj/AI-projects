import cv2
import imutils
img=cv2.imread("C:/Users/Balaji/Desktop/py3/tesim.webp")
cv2.imshow("tesla",img)
#cv2.imwrite("tesnew.jpg",img)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("teslagray",grayimg)
cv2.imwrite("graytes.jpg",grayimg)
resizeimg=imutils.resize(img,width=750)
#cv2.imshow("tesla2",resizeimg)

threshimg=cv2.threshold(grayimg,100,255,cv2.THRESH_BINARY)[1]
cv2.imshow("thrishtesla",threshimg)


