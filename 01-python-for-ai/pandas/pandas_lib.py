"""
Veri Bilimi Kütüphanesi
    -tablo şeklinde veri oluşturmak
    verileri düzenlemek ve filtrelemek
    sütun ve satir işlemleri yapmak
    dosyalardan veri okumak

pandas numpy ilişkisi
    numpy sayisal diziler sağlar , pandas tablo veri yapilari sağlar

    -series
    -dataframe
    -veri okuma ve yazma
    -veri seçme ve filtreleme
    -sütun ve satir işlemleri
    -veri siralama ve gruplama
"""
import pandas as pd

print("done")

"""
Series
"""

#seri oluşturma
veri = pd.Series([10 ,20 ,30 ,40])
print(veri)

"""
index   value
0       10
1       20
2       30
3       40

her bir veri indeks numarasıyla birlikte tutulur
"""

#seriler içindeki verilere erişme

veri = pd.Series([10,20,30,40])
print(veri[0])

#series için özel indeks belirleme

veri = pd.Series([10,20,30],index = ["a" , "b" , "c"])
print(veri["c"])

#dictionary ile seri oluşturma

veri = {
    "ali" : 80,
    "ayse" : 30,
    "sila": 87
}
print(veri)
s = pd.Series(veri)
print(s)

#series özellikleri

print(s.index) #index
print(s.values)
print(s.dtype)

#matematiksel işlemler

veri = pd.Series([10,20,30,40])
sonuc = veri * 2
print(sonuc)

#series filtreleme
yas = pd.Series([10,20,30,40,50])
filtre = yas > 25
print(filtre)
yasli = yas[yas > 25]
print(yasli)
#yaşlıları filtreleme
print(yas[filtre])

"""
Dataframe oluşturma
"""

veri = {
    "isim" : ["ali" , "ayşe" , "fatma"],
    "yas" : [10 , 20 , 30],
    "sehir" : ["istanbul" , "edirne" , "yalova"]
}
df = pd.DataFrame(veri)
print(df)

#sütun isimleri öğrenmek için
print(df.columns)

#dataframe satır sayısını öğrenme
print(df.shape)

#sütunlara erişim
print(df["isim"])

#birden fazla sütuna erişmek için
print(df[["isim" , "yas"]])

#yeni sütun ekleme , türkçe karakter ve büyük harf olmayacak

df["maas"] = [4000 , 6000 , 700]
print(df)

#sütun silme

df = df.drop("sehir" , axis = 1) #axis 0 sa satır axis 1 ise sütunlardı
print(df)

#ilk satırları görüntülemek için
print(df.head())#ilk 5 satırı gösterir

#sondaki satırları görüntülemek için
print(df.tail())

#dataframe hakkında bilgi alma
print(df.info())


"""
Dosya Okuma ve Yazma
"""
#csv (comma seperated values) dosyası okuma

df = pd.read_csv("veri.csv")
print(df)

#readle birçok dosyayı okuyabiliyoruz , Excel okuma 
df = pd.read_excel("veri_excel.xlsx")
print(df)


#csv dosyası yazma
veri = {
    "isim": ["ali" , "kaan" , "eren"],
    "yas": [25, 36 ,32]
}

df = pd.DataFrame(veri)
df.to_csv("veri_output.csv" , index =False) #index in gelmemesini istediğimiz durumlarda yapıyoruz

#excel dosyası yazma
df.to_excel("veri_output.xlsx", index = False)


"""
Veri Seçme Ve Filtreleme
"""

#örnek dataframe
veri = {
    "isim" : ["ali" , "ayse" , "mehmet" , "zeynep" , "ahmet"],
    "yas" : [10 , 15 , 25 , 35 ,34],
    "sehir" : ["ist" , "kocaeli" , "edirne" , "izmir" ,"mugla"],
    "maas" : [2000,2300,25000,26000,213124]
}
df = pd.DataFrame(veri)
print(df)

#sütun seçme
print(df[["isim" , "maas" , "sehir"]]) #eğer birden fazla seçmek istiyorsak iç içe 2 köşeli parantez yeterli

#satır seçme : iloc
print(df.iloc[0])


#birden fazla satır
print(df.iloc[0:3])

#satır seçme : loc
print(df.loc[2])

#belirli bir satır ve belirli bir sütun seçmek istersek
print(df.loc[:, ["maas" , "isim"]]) #tüm satırlar ama maaş ve isim sütunları sadece 

print(df.loc[:2, ["maas" , "isim"]]) #0 , 1 ve 2. satırlar ve maaş , isim sütunları sadece , (2 dahildir) 

#koşullu filtreleme
filtre = df["yas"] < 20
print(filtre)

sonuc = df[filtre]
print(sonuc)

#basit kullanımı 
print(df[df["yas"] > 30])

#birden fazla koşullu arama
#sehir kocaeli ve maas 6000 den fazla olan insanlar

sonuc = df[(df["sehir"] == "edirne") & (df["maas"] >= 6000)]
print(sonuc)

#belirli bir değeri içeren satırları getir
print(df[df["sehir"] == "kocaeli"])

#sadece belirli sütunları gösterme
#yaşı 25 den büyük olan verinin sadece isim ve maaşını göster

print(df[df["yas"] > 25][["isim","sehir"]])


"""
Sütun Ve Satir İşlemleri
"""

#dataframe oluştur
veri = {
    "isim" :["ali" , "ayşe" , "mehmet"],
    "yas":[25,30,27],
    "maas":[5000,7000,6000]
}
df = pd.DataFrame(veri)
print(df)

#yeni bir sütun ekleme
df["sehir"] = ["Ankara", "İstanbul" , "İzmir"]
print(df)

#hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12
print(df)

#sütun silme
df = df.drop("maas",axis =1)
print(df)

#sütun isim değiştirme
df = df.rename(columns={"yillik_maas": "yillikMaas"})
print(df)

#yeni satır eklemek
df.loc[3] = ["Zeynep" , 32 , "Ankara" , 5000]
print(df)

#satır silme
df = df.drop(0)
print(df)
#sildik fakat indeks 0 değeri de sıfırlandı , bunu istemeyiz

#index değerlerini yeniden düzenleme
df = df.reset_index(drop = True)
print(df)


"""
Veri Siralama ve Gruplama
"""

veri = {
    "isim" : ["ali" , "ayse" , "mehmet" , "zeynep" , "ahmet"],
    "yas" : [10 , 15 , 25 , 35 ,34],
    "sehir" : ["istanbul" , "istanbul" , "edirne" , "izmir" ,"izmir"],
    "maas" : [35000,2300,25000,26000,213124]
}

df = pd.DataFrame(veri)
print(df)

#veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)

#azalan sıralama
df_sirali = df.sort_values("maas", ascending=False)
print(df_sirali)

#birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir","maas"])#önce şehiri yazdığımız için önce şehire göre daha sonra şehirler içindeki maaşlara göre sıraladı
print(df_sirali)

#veri gruplama : groupby
#şehir bazında gruplama
gruplar = df.groupby("sehir")
print(gruplar)

#grupların ortalama maaşları
sonuc = df.groupby("sehir")["maas"].mean() #sehir bazında ortalama maaş hesaplama
print(sonuc)

#grupların toplam maaşları
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)

#grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)

#birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean" , "max" , "min"])
print(sonuc)

"""
Temel pandas Fonksiyonlari
"""
veri = {
    "isim" : ["ali" , "ayse" , "mehmet" , "zeynep" , "ahmet"],
    "yas" : [10 , 15 , 25 , 35 ,34],
    "sehir" : ["istanbul" , "istanbul" , "edirne" , "izmir" ,"izmir"],
    "maas" : [35000,2300,25000,26000,213124]
}
df = pd.DataFrame(veri)
#head fonksiyonuyla ilk 5 satırı görelim
print(df.head(3))#head in içine kaç satır görmek istiyorsak onu yazarız
print(df.tail(1))#sondaki satırları görmek için

#info()
print(df.info())#dataframe hakkında temel bilgilere ulaşılır , non-null kayıp veri olmadığı anlamına geliyor

#sayısal sütunların temel istatistiklerini görmek için describe()
print(df.describe())

#bir sütundaki değerlerin kaç kez tekrar ettiğini bulmak için value_counts() kullanılır
print(df["sehir"].value_counts())

#bir sütundaki benzersiz değerleri görmek için unique() kullanırız
print(df["sehir"].unique())

#bir sütunda kaç farklı değer olduğunu görmek için nunique() kullanırız
print(df["sehir"].nunique()) #3