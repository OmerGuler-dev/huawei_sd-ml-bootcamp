#belirli bir işi yapan ve çağrıldığında çalışan kod bloğudur
# sum() , max() , min()
sayilar = [1, 2 ,3 , 4 , 9 , 5 , 2]
print(sum(sayilar))
print(max(sayilar))

x = -2
print(abs(x)) #mutlak değer

print(sorted(sayilar))#sıralama

#build in pythonda olan fonksiyonlar , print mesela

#user defined * bizim yapacaklarımız

def selam_ver(isim , no , selam_ver = "Chat'e hoşgeldiniz."):
    print(f"Merhaba {isim} , {no} , {selam_ver}")

selam_ver("Ömer" , 25)
selam_ver("Kaan" , 34)
selam_ver("mahmood" , 21 , "Selam")


def topla(a, b):
    sonuc = a + b
    return sonuc

print(topla(3 , 5))

def hesapla(x , y):
    toplam = x + y
    carpma = x * y
    return toplam , carpma

hesapla_toplam , hesapla_carpma = hesapla(3 , 6)

print(hesapla_toplam)
print(hesapla_carpma)


#docstringlerin tanımlanması , ai agentlar bu docstringlere göre çalışacakları yere karar verirler
"""
Ornek Docstring

Konular:
- Değişkenler
- Koşullar
- Döngüler
- Fonksiyonlar
"""