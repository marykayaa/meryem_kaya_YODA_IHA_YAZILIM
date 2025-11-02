

# Kullanıcıdan bir cümle veya paragraf girmesini istiyoruz.
metin = input("Lütfen analiz etmek istediğiniz metni (cümle veya paragraf) girin:\n")


# 1. Toplam Karakter Sayısı Hesaplama (Boşluklar Dahil)
# len() fonksiyonu, bir dizedeki karakter sayısını (boşluklar ve noktalamalar dahil) verir.
toplam_karakter_sayisi = len(metin)

# 2. Metni Hazırlama ve Kelime Listesini Oluşturma

# BÜYÜK/KÜÇÜK HARF DUYARLILIĞI KARARI:
# Analizi büyük/küçük harf duyarsız yapmak için metnin tamamını küçük harfe çeviriyoruz.
# Örneğin, "Python" ve "python" aynı kelime olarak sayılacaktır.
temiz_metin = metin.lower()

# Noktalama işaretlerini kaldırarak kelime sayımını kolaylaştırıyoruz.

# .split() metodu boşlukları ve satır sonlarını otomatik olarak ayırır.
kelimeler = temiz_metin.split()

# 3. Toplam Kelime Sayısı Hesaplama

# Kelime listesinin uzunluğu bize toplam kelime sayısını verir.
toplam_kelime_sayisi = len(kelimeler)

# 4. Kelime Tekrarı (Frekans) Hesaplama (Sözlük Kullanımı)

# Kelime frekanslarını tutmak için boş bir sözlük (dictionary) oluşturuyoruz.
kelime_frekansi = {}

# Kelimeler listesi üzerinde tek tek döngü kuruyoruz (Loops: for).
for kelime in kelimeler:
    # Sözlükte o kelime daha önce varsa, değerini 1 artırıyoruz.
    if kelime in kelime_frekansi:
        kelime_frekansi[kelime] += 1
    # Sözlükte yoksa, kelimeyi yeni bir anahtar (key) olarak ekliyor ve değerini 1 yapıyoruz.
    else:
        kelime_frekansi[kelime] = 1


# 5. En Uzun Kelimenin Uzunluğunu Hesaplama

en_uzun_uzunluk = 0 # En uzun kelimenin uzunluğunu tutmak için başlangıç değeri 0.

# Kelimeler listesi üzerinde tekrar döngü kuruyoruz.
for kelime in kelimeler:
    # Mevcut kelimenin uzunluğunu (len(kelime)) kontrol ediyoruz.
    # Eğer bu kelimenin uzunluğu şu anki en_uzun_uzunluk değerinden büyükse...
    if len(kelime) > en_uzun_uzunluk:
        # en_uzun_uzunluk değerini güncelliyoruz.
        en_uzun_uzunluk = len(kelime)



print("\n--- METİN ANALİZ SONUÇLARI ---")
print(f"Toplam Karakter Sayısı (Boşluk Dahil): {toplam_karakter_sayisi}")
print(f"Toplam Kelime Sayısı: {toplam_kelime_sayisi}")
print(f"En Uzun Kelimenin Uzunluğu: {en_uzun_uzunluk}")
print("Büyük/Küçük Harf Duyarlılığı: Analiz BÜYÜK/KÜÇÜK HARF DUYARSIZ yapılmıştır.")

print("\n--- Kelime Tekrarları (Frekans) ---")

# .items() metodu, sözlükteki her anahtar-değer çiftini (kelime-tekrar) almanızı sağlar.
for kelime, tekrar in kelime_frekansi.items():
    print(f"'{kelime}': {tekrar} kez tekrar etti.")

print("---------------------------------")