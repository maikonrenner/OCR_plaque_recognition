import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\mrenner\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('ocr.png')
cv2.startWindowThread()
cv2.namedWindow("preview")
#pytesseract.image_to_string(img)
print(pytesseract.image_to_string(img))

# DETECTANDO OS CARACTERES

hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)    

cv2.imshow("preview", img)
cv2.waitKey()