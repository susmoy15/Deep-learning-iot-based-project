import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

save_path = 'susmoy/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

cap = cv2.VideoCapture(0)

def detect_face_and_save():
    count = 1500
    while count < 1600:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            cv2.imwrite(save_path + str(count) + '.jpg', roi_color)
            count += 1
            if count == 1600:
                break
        cv2.imshow('img', img)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

detect_face_and_save()
