import pandas as pd
"""

Örnek Veri Seti: 
    aşağidaki veri seti tüm sorular için kullanilacaktir
"""
veri = {
    "isim" : ["ali", "Ayşe" ,"Mehmet","Zeynep","Ahmet","Elif"],
    "yas" : [25,30,28,35,22,27],
    "sehir" : ["Ankara" ,"İstanbul","Ankara","İzmir","Bursa","İstanbul"],
    "maas" : [5000,7000,6000,8000,4500,6500]
}
df = pd.DataFrame(veri)
print("Veri Seti ")
print(df)
print("-" * 50)

#ilk 3 satır
#print(df.head(3))

#sütun isimlerini yazdırın
print(df.columns)

print(df["isim"])

print(df[["isim" , "maas"]])
 
print(df[df["yas"] > 25])


print(df[df["maas"]>6000][["isim","maas"]])

print("-" * 50)
print(df.sort_values("maas"))

print("*" * 50)
print(df.sort_values("maas" , ascending=False))


print("-" * 50)
print(df.groupby("sehir")["maas"].mean())


print("-" * 50)
df["yillikMaas"] = df["maas"] * 12
print(df)
print("-" * 50)