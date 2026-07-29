sayilar = [1 , 2 , 3 , 4]
isimler = ["omer" , "mehmet", "talha" , 12 , 25 , 35]

print(isimler)

print(sayilar[0:1]) #: dan sonrası dahil değil

print(sayilar[2:])# 2 den sonuna kadar

sayilar.append(5)
print(sayilar)

sayilar.insert(1,100)
print(sayilar)

sayilar.remove(100) #eleman silme
print(sayilar)

sayilar.pop() #en sondaki indeksteki değeri çıkarmaya çalışırken
print(sayilar)

sayilar[0] = 989 #belirli indeksteki değeri başka bir değerler değiştirmeye yarar
print(sayilar)
