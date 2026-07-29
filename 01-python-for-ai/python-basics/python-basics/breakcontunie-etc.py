for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    if i == 5:
        continue
    print(i)

#pass henüz kod yazmadığımız kısımda boş bırakmak için kullanılır

if True:

    pass

for i in range(3):
    if i == 1:
        pass
    print(i)


#nested yapılar , yapıların iç içe olması
yas = 23
ogrenci = True

if yas < 25:
    if ogrenci == True:
        print("Oğrenci indiirimi")



for i in range(20):
    if i > 10:
        if i % 2 == 0:
            print(f"Sayi {i} Büyük ve Çiftdir")
        else:
            print(f"Sayi {i} Büyük ve Tektir")
    else:
        if i % 2 == 0:
            print(f"Sayi {i} Küçük/Eşit ve Çifttir")
        else:
            print(f"Sayi {i} Küçük/Eşit ve Tektir")



for i in range(1,21):
    if i % 2 == 0:
        tur = "çift"
    else:
        tur = "Tek"

    if i > 10:
        boyut = "Büyük"
    else:
        boyut = "Küçük/Eşit"

    print(f"{i} = {tur} , {boyut}")            