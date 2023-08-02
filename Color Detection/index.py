import cv2 as cv
import utility
from PIL import Image

# by default we set ha blue color


blue = [255, 0, 0] 

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Error: Unable to open the camera.")
    exit(1)

while True:
    success, frame = capture.read()

    # convert the image into the hsv
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # get the bounds of the Selected Color
    lowerLimit, upperLimit = utility.GetBounds(color=blue)
    # mask the frame accoerding to the bounds
    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)
    # Make a rectagle on the mask
    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()
    if box is not None:
        x1, y1, x2, y2 = box
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    # flip the frame 
    frame = cv.flip(frame,1)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv.destroyAllWindows()
