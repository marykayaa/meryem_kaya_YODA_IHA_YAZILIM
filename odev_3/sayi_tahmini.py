


# random kütüphanesini rastgele sayı için içe aktarıyoruz.
import random

# Oyunun başlangıç mesajlarını 
print("=== Sayı Tahmini Oyununa Hoş Geldiniz! ===")
print("1 ile 100 arasında bir sayı tuttum. 10 hakkın var.")
print("============================================")

# 1 ile 100 (dahil) arasında rastgele bir tam sayı seçiyoruz.
rastgele_sayi = random.randint(1, 100)

# Toplam hak ve deneme sayacı.
maksimum_hak = 10
deneme_sayisi = 0

# Oyun döngüsünü başlatıyoruz. Hak bitene kadar devam edecek
while deneme_sayisi < maksimum_hak:
    
    # Kullanıcıdan GİRİŞ İSTEME 
    # Kullanıcının kaçıncı hakta olduğunu kullanıcıya gösterme
    tahmin_str = input(f"\nTahminini gir ({deneme_sayisi + 1}. deneme / {maksimum_hak} hak): ")
    
    # Basit bir kontrol: Kullanıcının sayı girdiğinden emin olmak için.
    if not tahmin_str.isdigit():
        print("Hatalı giriş! Lütfen sadece bir pozitif tam sayı girin.")
        continue # Döngünün başına döner, hak yanmaz.
        
    # Girdiyi tam sayıya çeviriyoruz.
    tahmin = int(tahmin_str)


    # Eğer tahmin 1'den küçük veya 100'den büyükse, hak kaybetmeden uyarırız.
    if tahmin < 1 or tahmin > 100:
        print("Geçersiz aralık! Tahminini 1 ile 100 ARALIĞINDA tutmalisin.")
        continue # Döngünün başına döner, hak yanmaz.


    # Eğer buraya geldiyse, tahmin geçerlidir ve aralıktadır. 
    deneme_sayisi += 1 

    # Doğru tahmin
    if tahmin == rastgele_sayi:
        print("\n*** TEBRİKLER! ***")
        print(f"Sayıyı {deneme_sayisi}. denemede doğru tahmin ettin!")
        break
    
    # Tahmin düşük
    elif tahmin < rastgele_sayi:
        print("Daha yüksek bir sayı tahmin et!")
    
    # Tahmin yüksek
    else: # tahmin > rastgele_sayi
        print("Daha düşük bir sayı tahmin et!")



# Eğer döngü haklar bittiği için sonlandıysa
if deneme_sayisi == maksimum_hak and tahmin != rastgele_sayi:
    print("\n--------------------------------------------")
    print("Tahmin hakların bitti. Üzgünüz, oyunu kaybettin!")
    print(f"Doğru sayı: {rastgele_sayi} idi.")
    print("--------------------------------------------")

print("\nOyun sona erdi.")