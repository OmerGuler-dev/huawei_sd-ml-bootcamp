"""
Bozuk veri Temizleme

veri : 
        70
        80
        abc
        90
        50
        hata 
        60
amaç = 
        -dosyayı oku
        -sayiya çevrilmeyen satirlari atla
        -geçerli notlari topla
        -ortalama hesapla
"""

with open("Veri.txt", "r" , encoding="utf-8") as f:
    liste = []
    hatali_veri = 0
    for satir in f:
            try:
                liste.append(int(satir.strip()))
            except ValueError :
                 print(f"Hatalı veri bulundu {satir.strip()}")
                 hatali_veri += 1
                
                 

print(f"notlar = {liste}")
print(f"hatali veriler = {hatali_veri}")

if liste:
    ortalama = sum(liste) / len(liste)
    print(ortalama)
else:
    print("listede geçerli sayi bulunamadi")



