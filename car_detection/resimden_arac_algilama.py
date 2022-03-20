import cv2

img=cv2.imread("C:\\udemyopencv\\haar_cascade\\test_images\\car.jpg")
body_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\car.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=body_cascade.detectMultiScale(gray,1.2,1)

for(x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Eye",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
