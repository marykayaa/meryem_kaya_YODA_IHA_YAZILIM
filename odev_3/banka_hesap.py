

#son 2 görevde ai kullanımına fazla yer vermek zorunda kaldım hyaptığım işlemleri anlayabiliyorum ancak kendim yazmaya calısırken sorun yasıyorum.



# Hesap işlemlerini yönetecek olan Sınıfı (Class) tanımlıyoruz.
# Sınıflar, nesneleri (bu durumda banka hesaplarını) tanımlayan şablonlardır.
class Hesap:
    
    # Sınıfın kurucu metodu (__init__). Bir nesne (hesap) oluşturulduğunda ilk çalışan fonksiyondur.
    # Bu metod, hesap sahibinin ilk bilgilerini ve başlangıç bakiyesini alır.
    def __init__(self, sahip_adi, hesap_no, baslangic_bakiye=0):
        # Nesne özelliklerini (instance attributes) tanımlıyoruz.
        self.sahip_adi = sahip_adi  # Hesap sahibinin adı
        self.hesap_no = hesap_no    # Hesap numarası
        self.bakiye = baslangic_bakiye # Hesabın güncel bakiyesi (Varsayılan: 0)
        print(f"\nYeni hesap başarıyla oluşturuldu. Hesap No: {self.hesap_no}")


    # Para yatırma işlemini gerçekleştiren metot (sınıfın fonksiyonu).
    def para_yatir(self, miktar):
        # Yatırılan miktarın pozitif olup olmadığını kontrol ederiz.
        if miktar > 0:
            # Bakiyeyi yatırılan miktar kadar artırırız.
            self.bakiye += miktar
            print(f"Başarıyla {miktar} TL yatırıldı.")
            self.bakiye_goruntule()
        else:
            print("HATA: Yatırılacak miktar pozitif olmalıdır.")


    # Para çekme işlemini gerçekleştiren metot.
    def para_cek(self, miktar):
        # Çekilmek istenen miktarın pozitif olup olmadığını kontrol ederiz.
        if miktar <= 0:
            print("HATA: Çekilecek miktar pozitif olmalıdır.")
            return # Fonksiyondan çıkarız.

        # Hesaptaki bakiyenin yeterli olup olmadığını kontrol ederiz.
        if self.bakiye >= miktar:
            # Bakiyeyi çekilen miktar kadar azaltırız.
            self.bakiye -= miktar
            print(f"Başarıyla {miktar} TL çekildi.")
            self.bakiye_goruntule()
        else:
            # Bakiye yetersizse uyarı veririz.
            print("HATA: Yetersiz bakiye.")
            self.bakiye_goruntule()


    # Hesabın güncel bakiyesini ekrana yazdıran metot.
    def bakiye_goruntule(self):
        print(f"\n--- Hesap Özeti ---")
        print(f"Hesap Sahibi: {self.sahip_adi}")
        print(f"Hesap No: {self.hesap_no}")
        print(f"Güncel Bakiye: {self.bakiye} TL")
        print(f"-------------------")
        
    # Hesap nesnesinin string olarak temsil edilme şeklini belirler (Opsiyonel ama kullanışlı).
    def __str__(self):
        return f"Hesap Sahibi: {self.sahip_adi}, Hesap No: {self.hesap_no}"


print("=== Yeni Banka Hesabı Oluşturma ===")
sahip_adi = input("Hesap sahibinin adını ve soyadını girin: ")
hesap_no = input("Hesap numarasını girin (Örn: 123456): ")

#  başlangıç bakiyesi alımı
while True:
    try:
        baslangic_bakiye = float(input("Başlangıç bakiyesini girin (Varsayılan 0): "))
        if baslangic_bakiye < 0:
            print("Bakiye negatif olamaz.")
            continue
        break
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer girin.")

# Hesap sınıfından bir nesne (object) oluşturuyoruz.
# Bu işlem, __init__ metodunu otomatik olarak çağırır.
kullanici_hesabi = Hesap(sahip_adi, hesap_no, baslangic_bakiye)


# 2. Hesap Yönetimi Menüsü (Loops: while True)
while True:
    print("\n\n--- İşlemler Menüsü ---")
    print("1: Bakiye Görüntüleme")
    print("2: Para Yatırma")
    print("3: Para Çekme")
    print("4: Çıkış")
    
    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

    
    if secim == '1':
        # Bakiye görüntüleme metodunu çağırırız.
        kullanici_hesabi.bakiye_goruntule()
        
    elif secim == '2':
        # Para yatırma
        try:
            miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            kullanici_hesabi.para_yatir(miktar)
        except ValueError:
            print("Geçersiz miktar girişi.")

    elif secim == '3':
        # Para çekme
        try:
            miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            kullanici_hesabi.para_cek(miktar)
        except ValueError:
            print("Geçersiz miktar girişi.")
            
    elif secim == '4':
        # Çıkış işlemi
        print("\nProgramdan çıkılıyor. Bizi tercih ettiğiniz için teşekkürler!")
        break # Döngüyü sonlandırırız.
        
    else:
        # Geçersiz menü seçeneği
        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir numara girin.")

# Program sonlanır.