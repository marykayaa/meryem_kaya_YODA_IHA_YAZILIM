


def hesapla(sayi1, sayi2, islem):
    # İşlem 

    if islem == '+':
        return sayi1 + sayi2
    
    elif islem == '-':
        return sayi1 - sayi2
    
    elif islem == '*':
        return sayi1 * sayi2
    
    elif islem == '/':
        # Sıfıra bölme kontrolü
        if sayi2 == 0:
            return "HATA: Bir sayı sıfıra bölünemez."
        else:
            return sayi1 / sayi2
    
    else:
        return "HATA: Geçersiz işlem operatörü."

# Kullanıcıdan sayısal girdi almayı garantileyen yardımcı fonksiyon.Bu kısmı ai ie ilerlettim tamamen
def sayi_girisi_al(prompt):
    # Sayısal bir girdi alınana kadar döngüyü sürdürür (while True).
    while True:
        girdi = input(prompt)
        
        # Girdiyi doğrudan float'a çevirmeyi deneriz. 
        # Float() tam sayıyı ve ondalıklı sayıyı kabul eder.
        # Bu, try-except'i simüle etmenin dolaylı bir yoludur.
        try:
            return float(girdi)
        except ValueError:
            # Dönüşüm başarısız olursa, kullanıcıyı uyarır ve döngünün başına döner.
            print("Geçersiz giriş! Lütfen sayısal bir değer girin.")


print("=== Basit Hesap Makinesi ===")

while True:
    
    # ilk sayıyı alıyoruz.
    sayi1 = sayi_girisi_al("İlk sayıyı girin: ")
    
    # İşlem operatörünü alıyoruz.
    islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")
    
    # ikinci sayıyı alıyoruz.
    sayi2 = sayi_girisi_al("İkinci sayıyı girin: ")
    
    # Hesaplama işlemini gerçekleştiriyoruz.
    sonuc = hesapla(sayi1, sayi2, islem)

    # Sonucu ekrana yazdırıyoruz.
    print(f"\nSonuç: {sonuc}")


    
    # Kullanıcıya devam etmek isteyip istemediğini soruyoruz.
    devam = input("\nBaşka bir işlem yapmak ister misiniz? (E/H): ").lower()
    
    # Kullanıcı 'h' (Hayır) girerse döngüyü sonlandırırız.
    if devam == 'h':
        print("Hesap makinesi kapatılıyor. Güle güle!")
        break