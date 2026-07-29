"""
Dosya işlemleri :
    -dosyadan veri okuma
    -okunan verinin işlenmesi
    -dosyaya veri yazma ve kaydetme
    -with yapisi

    Yapay zeka veriden öğrenir bu yüzden dolayi veriyi python ortamina yüklememiz ve işlememiz lazim
"""

#dosya = verinin kalıcı olarak saklandığı yapılardır

dosya = open("ornek.txt" , "r" , encoding="utf-8")
icerik = dosya.read()
print(icerik)
dosya.close()


#satır satır okuma
dosya = open("ornek.txt", "r", encoding="utf-8")

for satir in dosya:
    print(satir.strip())

dosya.close()

dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

print(icerik)
yeni_icerik = icerik.upper()
print(f"yeni_icerik = {yeni_icerik}")

dosya = open("ornek.txt", "r", encoding="utf-8")
satirlar = dosya.readlines()
dosya.close()

print(f"Toplam Satır sayısı = {len(satirlar)}")

#Yazma İŞLEMLERİ


dosya = open("yeni_dosya.txt", "w" , encoding= "utf-8")
dosya.write("Merhaba")
dosya.write("\nPython machine learning")
dosya.close()

#veri işleme

dosya = open("islenmis_ornek.txt" , "r" , encoding= "utf-8")
icerik = dosya.read()
dosya.close()
print(icerik)

dosya = open("islenmis_ornek.txt", "w" , encoding= "utf-8")
dosya.write("\n Icine yazdirdigimiz veri")
dosya.close()

dosya = open("islenmis_ornek.txt" , "r" , encoding= "utf-8")
icerik = dosya.read()
dosya.close()
print(icerik)



