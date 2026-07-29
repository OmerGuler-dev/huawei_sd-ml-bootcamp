sayilar = [10 , 20 ,30]

for i in sayilar:
    print(i + 5) 


for i in range(1 , 7):
    print(i)

toplam = 0
for i in sayilar:
    toplam = toplam + i
    print(toplam)

print(toplam)


pozitif = [1 , 2, 3 ,4 , 5 , 6]

for sayi in pozitif:

    if sayi % 2 == 0:
        print(f"Sayi Çifttir : {sayi}")
    else:
        print(f"Sayi tektir : {sayi}")


kelime = "machine"

for i in kelime:
    print(i)