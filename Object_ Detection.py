import cv2
import time
import imutils
cam = cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
area = 800

while True :
    _,img= cam.read()
    text= "Normal"
    img = imutils.resize(img, width=800)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianimg = cv2.GaussianBlur(grayimg,(21,21),0)
    if firstFrame is None :
        firstFrame =gaussianimg
        continue
    imgDiff = cv2.absdiff(firstFrame ,gaussianimg)
    threshimg= cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    threshimg = cv2.dilate(threshimg,None, iterations = 2)
    cnts = cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts= imutils.grab_contours(cnts)
    for d in cnts:
        if cv2.contourArea(d)< area:
             continue
        (x,y,w,h)= cv2.boundingRect(d)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text ="Moving object detect"
        print (text)
        cv2.putText (img, text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        cv2.imshow(" camera feed", img)
        key = cv2.waitKey(1) & 0xFF
        if key ==ord("q"):
            break
    

cam.release()
cv2.destroyAllWindows()
