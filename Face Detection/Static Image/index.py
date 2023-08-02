import cv2 as cv

det = cv.CascadeClassifier('Data/haarcascade_frontalface_default.xml')

img = cv.imread('Data/random-group-photo.jpg')

img = cv.resize(img,(700,500))

cv.imshow("Simple Image ",img)

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = det.detectMultiScale(gray_img,1.1,4)

for x,y,w,h in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    


cv.imshow("Detected Image",img)

cv.waitKey(0)
cv.destroyAllWindows()