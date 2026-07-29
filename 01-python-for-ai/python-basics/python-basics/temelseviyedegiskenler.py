print("Hello world \n")

yas = 35

print(yas)
a = 10
b = 5
toplam = a + b
carpma = a * b
print(toplam , carpma)

birim_fiyat = 10

urun_sayisi = 8

toplam = urun_sayisi * birim_fiyat

print("toplam stoktaki değer miktarı : ", toplam)

yuzde = int(input("Yeni yüzde değeri ne kadar olsun : "))

zamlifiyat = birim_fiyat + birim_fiyat*yuzde/100

print("Yeni zamli fiyatı ", zamlifiyat)
sonuc = 24.1231
sonuc_yuvarlanmis = round(sonuc, 2)

fiyat = float(input("Fiyat giriniz : "))
print(fiyat)
kdvli_fiyat = round(fiyat + 20*fiyat/100 , 2)
print(kdvli_fiyat)

isim = "kaan"
yas = 31

sonuc = isim + " Hocanin yasi : " + str(yas) 
print(sonuc)

accuracy = 95
print(f"Doğruluk orani = {accuracy}")