

Nesne Tespiti 

Nesne Tespitinde Tarihsel Dönüm Noktaları


R-CNN (2014): Nesne tespitinde derin öğrenmenin ciddi şekilde kullanılmaya başlaması burada oldu. Görüntüdeki bölgeler önce belirleniyor, sonra her bölge CNN’e veriliyordu. Yavaş ama devrim niteliğinde.

Fast R-CNN (2015): Tüm görüntüden tek seferde özellik çıkarıyor, bu yüzden R-CNN’e göre çok hızlı.

Faster R-CNN (2015): Region Proposal Network (RPN) ekleyerek bölgeleri modelin kendi çıkarmasını sağladı. Hem hız hem doğruluk arttı.

YOLO (2015 →): “You Only Look Once”. Tüm görüntüye tek seferde bakıyor ve hem sınıf hem konum tahminini aynı anda yapıyor. En hızlı modellerden biri. Gerçek zamanlı uygulamalarda çok tercih ediliyor.

SSD (Single Shot Detector): Tek aşamalı başka bir model. Farklı boyuttaki feature maplerden tahmin yapıyor. Hem hızlı hem pratik.

RetinaNet (2017): One-stage modellerin doğruluk sorununu Focal Loss ile çözmeye çalıştı. Bu loss özellikle pozitif/negatif örnek dengesizliğini azaltıyor.

DETR (2020): Transformer tabanlı ilk büyük nesne tespit modeli. NMS, anchor gibi eski yöntemleri ortadan kaldırıp daha düzenli bir yapı sunuyor.

CNN Tabanlı Modellerin Mantığı ve Önceki Yöntemlerden Farkı

CNN’ler derin öğrenmeden önceki yöntemlere göre çok farklı bir yaklaşım getiriyor.

Önceki yöntemlerde (HOG, SIFT, Haar vb.):

Özellikler elle çıkarılıyordu.

Model sadece sınıflandırma yapıyordu, özelliğin ne olduğuna kendisi karar veremiyordu.

CNN’lerde ise:

Özellik çıkarma tamamen otomatik ve öğrenilebilir.

Konvolüsyon filtreleri görüntüdeki kenar, doku, şekil gibi bilgileri kendi öğreniyor.

Daha derin katmanlarda daha karmaşık özellikler ortaya çıkıyor.

Bu yüzden CNN tabanlı modeller klasik yöntemlere göre çok daha başarılı oluyor.

Kullanılan Modeller ve Genel Özellikleri
Two-Stage Modeller:

Faster R-CNN:

Önce bölge önerisi, sonra sınıflandırma yapıyor.

Genel olarak daha yüksek doğruluk veriyor.

Ama hız olarak one-stage modellere göre daha yavaş.

One-Stage Modeller:

YOLO ailesi:

Çok hızlı. Gerçek zamanlı çalışabiliyor.

Yeni sürümleri doğrulukta da oldukça iyi.

SSD:

Hızlı ve hafif.

Mobil cihazlar için uygun versiyonları var.

RetinaNet:

Focal Loss sayesinde zor ve dengesiz veri setlerinde avantajlı.

Transformer Tabanlı Modeller:

DETR:

Daha sade bir pipeline.

Global ilişkileri iyi öğreniyor.

Eğitim süresi klasik modellere göre biraz uzun olabiliyor.

Avantaj – Dezavantaj Özetim

Two-Stage Modeller (ör. Faster R-CNN):

Daha yüksek doğruluk

Zor sahnelerde güçlü – Daha yavaş

One-Stage Modeller (YOLO, SSD, RetinaNet):

Çok hızlı

Gerçek zamanlı uygulamalar için ideal – Bazıları iki aşamalı modellere göre biraz daha düşük doğruluk verebiliyor (ama fark giderek kapanıyor)

Transformer Tabanlılar (DETR):

Daha temiz bir yapı

Anchor/NMS yok – Eğitimi daha uzun sürebiliyor



Hangi Model Ne Zaman Tercih Edilir?

Gerçek zamanlı uygulama (kamera, robotik, canlı takip): YOLO veya SSD

En yüksek doğruluk gerekli olduğunda: Faster R-CNN

Dengesiz veri setlerinde: RetinaNet

Araştırma amaçlı modern yapı isteyen: DETR