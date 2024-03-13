##import cv2
##vs=cv2.VideoCapture(1)
##while True:
##    _,img=vs.read()
##    cv2.imshow("vvdo",img)
##    key=cv2.waitkey(1)&0xFF
##    if key==ord("q"):
##        break
##vs.release()
##cv2.destroyAllWindows()

import cv2

vs = cv2.VideoCapture(0)

while True:
    _, img = vs.read()
    cv2.imshow("video", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
