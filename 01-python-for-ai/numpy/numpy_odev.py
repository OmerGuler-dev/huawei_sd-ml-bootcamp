import numpy as np

dizi = np.arange(1,21)
print("dizi" , dizi)
print(dizi.size)

sayilar = [5, 10 ,15,20,25]
dizi = np.array(sayilar)
carpim = dizi * 3
print(carpim)

dizi = np.arange(0 , 31)
secilen = dizi[10:21]
print(secilen)#slicing

a = np.array([1 , 2 , 3])
b = np.array([4, 5, 6])
birlesmis = np.concatenate((a,b))
print(birlesmis)

dizi = np.arange(1 , 13)
matris = dizi.reshape(3 , 4)
print(matris)

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a[1])
print(a[:,1])

a = np.random.rand(3 , 3)
print(np.max(a))
print("Ortalaması = " ,np.mean(a))

a = np.array([2,4,6,8])
b = np.array([1,3,5,7])
sonuc = a*b
print(sonuc)


a = np.arange(1,10)
matris = a.reshape(3,3)

transpose = matris.T
print("Transpose : " ,transpose)


#son soru 

dizi = np.random.randint(1,51,10)
print("rastgele sayilar = ", dizi)
print("Toplam = ", np.sum(dizi))
print("Ortalamasi = ", np.mean(dizi))