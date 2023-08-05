import cv2
siu = cv2.imread("poster.jpg")
rocket = siu[120:360,400:500]
siu[0:240,500:600] = rocket
siuu = "my name is pratyaksh chauhan i study in class 7"
cv2.putText(siu,siuu,(20,220),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(245,245,245))
cv2.imshow("rocket",rocket)
cv2.imshow("output",siu)
cv2.waitKey(0)

