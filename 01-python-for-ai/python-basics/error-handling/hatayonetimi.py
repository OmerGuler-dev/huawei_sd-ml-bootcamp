"""
    Hata Yönetimi:
        - hata (error) ve istisna (exception)

    hata yönetimi program çökmeden kontrollü bir şekilde çalişmasini sağlar

    yapay zekada ,
        veri hazirlama
        dosya okuma
        model eğitim döngüsü
        rag sistemleri
"""

#if 5 > 3:
#    print("ok")
#name error

# print(x)

#type error
#print("10" + 5)


#value error
#int("Kaan")

#zero division hatası

#indeks hatası
liste =[1, 2 ,3 ,4]
#print(liste[10])

#key error = sözlükte anahtar hatası
ogrenci = {"isim": "Kaan"}
#print(ogrenci["yas"])

#file not found hatası
#with open("Kaan.txt" , "r")as f:
    #print(f.read())

#attribute hatası , yanlış metot özellik hatası
sayi = 10
#sayi.append(5)

#try , except , else , finally

"""
try - except
    -program hata verdiğinde durmasını istemeyiz
    -hata olursa yakalayıp kontrollü şekilde yönetmesi lazım
"""
try:
    sayi1 = int(input("sayi giriniz : "))
    print(10/sayi1)
except ValueError:
    print("Bir sayı giriniz")
except ZeroDivisionError:
    print("Sıfırdan farklı bir sayı giriniz")


#else hata yoksa çalışır
try:
    sayi = int(input("sayi giriniz : "))
    sonuc = 10/sayi
except ValueError:
    print("Bir sayı giriniz")
except ZeroDivisionError:
    print("Sıfırdan farklı bir sayı giriniz")
else:
    print(f"sonuç = {sonuc}")

#finally her durumda çalışır

try: 
    dosya = open("veri.txt" , "r", encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    try:
        dosya.close()
    except:
        pass

yas = int(input("Yaş : "))

if yas < 0:
    raise ValueError("Yaş sıfırdan küçük olamaz")

#genel hata ayıklama

try:
    sayi = int(input("Bir sayi giriniz : "))
    print(10/sayi)
except Exception as e :
    print(f"Hata : {str(e)}")