import cv2
import numpy as np
import time


CASCADE_FILE = 'odev_4/haarcascade_frontalface_default.xml' 

face_cascade = cv2.CascadeClassifier(CASCADE_FILE)

if face_cascade.empty():
    print(f"KRİTİK HATA: Yüz tespit dosyası yüklenemedi! Yol: {CASCADE_FILE}")
    print("Lütfen 'haarcascade_frontalface_default.xml' dosyasının 'goruntu_ısle_uygula.py' dosyasıyla AYNI klasörde (odev_4) olduğundan emin olun.")
    exit()


cap = cv2.VideoCapture(0)


center_points = []
MAX_POINTS = 60 

start_time = None       
tracking_started = False 


if not cap.isOpened():
    print("HATA: Kamera açılamadı! Başka bir uygulamanın kamerayı kullanmadığından emin olun.")
else:
    print("Kamera erişimi başarılı. Pencere açılıyor...")

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Görüntü yakalanamıyor veya kamera bağlantısı kesildi.")
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(50, 50)
        )

    
        
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            
       
            center_x = x + w // 2
            center_y = y + h // 2
            
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            
            coord_text = f"Merkez: ({center_x}, {center_y})"
            cv2.putText(frame, coord_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            center_points.append((center_x, center_y))
            if len(center_points) > MAX_POINTS:
                center_points.pop(0) 

            for i in range(1, len(center_points)):
                pt1 = center_points[i - 1]
                pt2 = center_points[i]
                cv2.line(frame, pt1, pt2, (255, 0, 0), 2) 
            
            if not tracking_started:
                start_time = time.time()
                tracking_started = True

        else:
          
            tracking_started = False
            center_points = [] 

       
        elapsed_time = 0.0
        if tracking_started and start_time is not None:
            elapsed_time = time.time() - start_time
            timer_text = f"Tespit Suresi: {elapsed_time:.1f} sn"
            color = (0, 255, 255) 
        else:
            timer_text = "Yuz Tespit Edilemedi"
            color = (0, 0, 255) 

        (text_w, text_h), baseline = cv2.getTextSize(timer_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        cv2.putText(frame, timer_text, 
                    (frame.shape[1] - text_w - 10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

       

        cv2.imshow('Yuz Takip Uygulamasi', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()