#değiştirilemezler , birden fazla veriyi kapsar , listeye benzer

renkler = ("kirmizi" , "mavi", "yeşil")

t = (10 , 20 ,30 , 40)
print(t[1:3])

x = (5 , 10 , 20)
print(type(x)) #eğer bir eleman varsa , içinde ne varsa o (mesela int se int) birden fazla varsa tuple

koordinat = (10 , 20 , 2)
x, y , z= koordinat
print(x)
print(y)
print(z)

t = (20 , 20 , 30 ,40)

print(t.count(20))
print(t.index(40))

#sözlükler , key value olayı

ogrenci = {
    "isim" : "ali",
    "yas" : 25,
    "bolum" : "bilgisayar"
} 
print(ogrenci)

#dictionary de : olarak kullanırız tanımlamalardan sonra

print(ogrenci["isim"])
print(ogrenci["yas"])

#yeni değer eklemek için

ogrenci["not"] = 85
print(ogrenci)

#güncellemek için

ogrenci["yas"] = 26
print(ogrenci)

#eleman silmek için

del ogrenci["bolum"]
print(ogrenci)

print(ogrenci.keys()) 
print(ogrenci.values())
print(ogrenci.items())

#anahtarlar , anahtarların deperleri , ve anahtar ve değerleri birlikte görmek için kullanılır


#set yapısı , benzersiz unique elemanlardan oluşan bir veri yapısıdır 

sayilar = {1 , 2, 3 ,4}
print(sayilar)

sayilar = {1 , 2 , 3 , 3 , 4 , 4, 5 , 5}
print(sayilar)

#tekar edenleri almaz ,benzersiz olması lazım , süslü parantez kullanılır , set de indeks de yoktur

liste = [1 , 2 , 3 ,3 ,4 , 4 ,5 ,5 ,6]
benzersiz = set(liste)
print(benzersiz)

#listeyi set e  çevirdik 


sayilar.add(7)
print(sayilar)

sayilar.remove(2)

#set işleri genelde birleşim , kesişim ve fark bulmalarda kullanılır

a = {1 , 2 , 3}
b = {3 , 4 , 5}

print(" ")
print(a.union(b)) #birleşim

print(a.intersection(b)) #kesişim

print(a.difference(b)) #farkı
