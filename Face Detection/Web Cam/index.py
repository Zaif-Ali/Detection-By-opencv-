import cv2 as cv

capture = cv.VideoCapture(0)

Detec = cv.CascadeClassifier("Data/haarcascade_frontalface_default.xml")

if not capture.isOpened() : 
    print("Problem in capture")
    exit(1)

while True:
    success , frame = capture.read()

    if not success:
        print("Some problem occurring to getting frames")
        break

    frame = cv.resize(frame,(450,450))
    frame = cv.flip(frame,1)
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = Detec.detectMultiScale(grayframe,1.1,4)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv.imshow("detected frame",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

