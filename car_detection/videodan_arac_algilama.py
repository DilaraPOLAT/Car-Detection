import cv2
#haar cascade cok ıyı bir performans gostermez
cap = cv2.VideoCapture("C:\\udemyopencv\\haar_cascade\\test_videos\\car.mp4")
car_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\car.xml")  # cascade dosyamı ekledim

while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,360))#botyutu degistirdik aslında tespit dahada zorlasır
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    cars = car_cascade.detectMultiScale(gray, 1.2,2)  # bu cascade dosyasını kullanıp resimdeki yuzun koordinatlarını bul
    # img,olceklendirme degeri=kac oranda resmi kucultecegim ,belli bir bolgede en az 4 pencere bulsun ben onun yuz oldugunu anlayayım
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0XFF == ord("q"):
        break

cap.release()  # videoyu serbest bırakıyorum eger bunu yapmazsam ne olur? videoyu kullanamam hata verir video baska bir islem icin calısıyor.
cv2.destroyAllWindows()