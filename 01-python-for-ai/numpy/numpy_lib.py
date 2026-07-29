"""
Numpy : 
    yüksek performansli sayisal hesap kütüphanesi
    büyük veri , hizli matematik , matris hesaplamalari , bilimsel ve istatiksel işlem


    -scikit-learn (ml)
    -tensorflow ve pytorch (dl)
    -pandas(data science)

    *diziler
    *matematiksel işlemler
    *indeksleme ve dilimleme
    *dizi birleştirme ve bölme
    *çok boyutlu diziler
    *matris işlemleri 
    *rastgele sayi üretimi
"""

import numpy as np

"""
Diziler(array)
    -ndarray = n-dimensional array
"""

sayilar = [1 , 2 , 3, 4 , 5] #liste
print(sayilar)

dizi = np.array(sayilar) # np.array python dizisini numpy listesine dönüştürüyor
print(dizi)

print(type(dizi))

#numpy dizisi boyutu öğrenme
print(dizi.shape) #(5, ) 5 elemanlı tek boyutlu dizi

#numpy dizisinin veri tipi

print(dizi.dtype) #int64 = integer

#numpy ile dizi oluşturma

dizi = np.zeros(5)
print(dizi)

dizi = np.ones(5)
print(dizi)

#belirli bir aralıkta sayı dizisi oluşturma

dizi = np.arange(0 , 10) #0 dan 10 a kadar
print(dizi)

dizi = np.arange(0 , 10 , 2)
print(dizi)

#belirli bir aralığa eşit bölünmüş diziler

dizi = np.linspace(0 , 10 , 5) # 10 alana dahil
print(dizi)

"""
Matematiksel İşlemler
"""

a = np.array([1 , 2 , 3])
b = np.array([4 , 5 , 6])
sonuc = a + b
print(sonuc)

cikarma = a - b
print(cikarma)

carpma = a * b
print(carpma)

bolme = a / b
print(bolme)

kare = a ** 2
print(kare)

#karekökünü alalım

a = np.array([1 , 4 ,9 , 16 ])
sonuc = np.sqrt(a)
print(sonuc)

#dizinin toplamını alma
print(np.sum(a))

print(np.mean(a))

print(np.max(a))
print(np.min(a))

#standart sapma
print(np.std(a))


"""
indeksleme (indexing) - dilimleme (slicing)
"""
#dizilerde indeksleme

dizi = np.array([10 , 20 , 30 ,40 , 50 , 60])
print(dizi[0])

#negatif indeksleme 

print(dizi[-1])

#slicing (dilimleme)
print(dizi[1:4]) # 4 dahil değil
print(dizi[3:])# 3 den başla sonuna kadar git
print(dizi[:3])# 0 dan başla 3 e kadar git

print(dizi[::2]) #2 şer adımla eleman seçme

#2 boyutlu diziler

matris = np.array(
    [
        [1 , 2 , 3],
        [4, 5 ,6],
        [7 , 8 , 9]
    ]
)
print(matris)
print(matris[0][0])
print(matris[0][1])
print(matris[1 , :])#belirli bir satır seçme

print(matris[: , 2])#belirli bir sütun seçme

#matris dilimleme işlemleri 

print(matris[0:2, 0:2])#[satır , sütun]

matris = np.array(
    [
        [1 , 2 , 3 , 4],
        [5 , 6 , 7 , 8],
        [9 , 10 , 11 , 12]
    ]
)
print(matris)
print(matris[0:3 , 0:2])#[satır , sütun]
print(matris[1 , :])
print(matris[ : , 1])

"""
Dizi birleştirme ve Bölme
"""
a = np.array([1, 2 ,3])
b = np.array([4, 5 ,6])

sonuc = np.concatenate((a,b))#np.concatenate birleştirme işine yarar
print(sonuc)

#iki boyutlu dizi birleştirme

a = np.array(
    [
        [1 , 2],
        [3 , 4]
    ]
)
b = np.array(
    [
        [5 , 6],[7, 8]
    ]
)
sonuc = np.concatenate((a,b))
print(sonuc) #varsayılan olarak satır yönünde birleştirdik

#axis parametresi 
#axis = 0 -> satır yönünde birleştirme
#axis = 1 -> sütun yönünde birleştirme

sonuc = np.concatenate((a , b),axis = 1)
print(sonuc)

#vstack (dikey birleştirme)

sonuc = np.vstack((a, b))
print(sonuc)

#hstack (yatay birleştirme)
sonuc = np.hstack((a , b))
print(sonuc)

# diziyi parçalara bölme 

dizi = np.array([1,2,3,4,5,6])
sonuc = np.split(dizi , 2)# eğer tek sayı olsaydı 2 ye bölüm işlemini yapmayıp hata verecekti
print(sonuc)

matris = np.array(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]
)
sonuc = np.split(matris,2) #satır bazıdan ikiye bölme
print(sonuc)

sonuc = np.split(matris,2 , axis = 1) #sütun bazıdan ikiye bölme
print(sonuc)

#Çok boyutlu Dizi oluşturma
matris = np.array(
    [
        [1,2,3],
        [3,4,5],
        [5,6,7]
    ]
)
print(matris)
#dizinin boyutunu öğrenme
print(matris.shape)#shape bu alttaki ikisinin de görevini yapıyor aslında

#dizinin kaç boyutlu olduğunu öğrenmek
print(matris.ndim)

#dizideki eleman sayısı
print(matris.size)

#3 boyutlu dizi oluşturma
dizi3 = np.array(
    [
     [
      [1,2],
      [3,4]
     ],
     [
     [5,6],
     [7,8]
     ]
    ]
 )
print(dizi3)
print(dizi3.shape)
#2 adet matris , her matriste 2 satır , her satırda 2 sütun vardır

#numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(12)
print(dizi)

#matrise dönüştürme
matris = dizi.reshape(3,4)
print(matris)

"""
Matris işlemleri : 
"""

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(a + b)
print(a - b)

#gerçek matris çarpımı 

sonuc = np.dot(a , b)#normal matris çarpımı , birincinin satırıyla 2.nin sütunu şeklinde
print(sonuc)

#matris Transpose (matrisin ters çevrilmesi) 
print(a.T)#satırlarla sütunların yer değiştirmesi olarak hatırla

#matris determinantı
det = np.linalg.det(a)
print(det)

#matrisin ters
ters = np.linalg.inv(a)
print(ters)

#rastgele sayi üretme

rastgele = np.random.rand(5)#rastgele 5 ondalık sayı üretmiş olduk , 0 ile 1 arasında
print(rastgele)

rastgele = np.random.rand(3, 3)
print(rastgele)

#rastgele tam sayı üretme
rastgele = np.random.randint(1 , 10 , 5)#1 ile 10 arasında 5 adet tam sayı üret
print(rastgele)

rastgele = np.random.randint(1 , 20 , (3 , 4))#1 ile 20 arasında 3 e 4 lük rastgele matriş üretir
print(rastgele)

#aynı rastgele sonucu üretmek için
np.random.seed(42) #aynı sonucu üretmeye yarayan fonksiyon
rastgele = np.random.rand(5)
print(rastgele)#makine öğrenmesi deneylerinde sıkça kullanılır

#bir diziden rastgele seçim yapma
dizi = np.array([10,20,30,40,50])
secim = np.random.choice(dizi)
print(secim)

#birden fazla eleman seçme

secim = np.random.choice(dizi , 3)
print(secim)
