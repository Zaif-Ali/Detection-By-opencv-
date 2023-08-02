import cv2 as cv
import qrcode as qr

# data whose store in the qr code
data = 'https://github.com/Zaif-Ali'

# setting the qr code 
qr = qr.QRCode(
    border=1,
    version=7,
    box_size=40,
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save("Data/qrcodeExample.png")

# Reading the qrcode with opencv

detector = cv.QRCodeDetector()

# read the image in the gray mode 
img = cv.imread('Data/qrcodeExample.png', 0)

retrval,  info, points, _ = detector.detectAndDecodeMulti(img)

# info get in the form of tuple 
print(info[0])
