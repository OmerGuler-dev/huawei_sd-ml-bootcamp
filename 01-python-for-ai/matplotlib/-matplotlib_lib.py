"""
Matplotlib
    görselleştirme
    veriyi anlama için görselleştirme

matplotlib ile neler yapilabilir
    -line , sütun , pasta , dagilim

matplotlib = görselleştirme
numpy = sayisal işlemler
pandas = tablo , veri yapilari

    örnek veri işleme süreci
        veri okunur(pandas)
        veri düzenleme(pandas)
        veri üzerine işlemler yapilir(numpy/pandas)
        veri grafikler ile gösterilir(matplotlib)


    *line plot(çizgi)
    *bar chart(sütun)
    *pie chart (pasta)
    *scatter plot(dagilim)
    *subplots
"""

import matplotlib.pyplot as plt
"""

#line plot (çizgi grafiği) , zamana göre değişen değerleri görselleştirmek için kullandığımız grafiktir

"""
#line plot
"""
#çizgi grafiği
gunler = [1 , 2 , 3, 4, 5]
sicaklik = [20 ,22, 21, 23, 25]

#marker noktaları belirliginleştirmek için
plt.plot(gunler,sicaklik, color = "red" , linestyle = "--" , marker = "o") # (x = gunler , y = sicaklik)
plt.title("Günlere Göre Sicaklik Grafiği")
plt.xlabel("Günler")
plt.ylabel("Sicaklik")
plt.grid(True)#çizgili hale getirir
plt.show()#grafiği en son ekranda görselleştirdiğimiz kısım

"""
"""
"""
#Bar Chart (sütun grafikleri) = kategorik verileri karşilaştirmak için kullanilir
"""
isimler = ["ali" , "Ayşe" , "mehmet" , "hasan"]
notlar = [70 , 60 ,95 ,25]

renkler = ["red" , "orange" , "yellow" , "blue"]
plt.bar(isimler , notlar, color = renkler)# (x , y)
plt.title("Öğrenci Notlari")
plt.xlabel("isimler")
plt.ylabel("notlar")
plt.show()

#yatay sütun grafiği
plt.barh(isimler,notlar)
plt.show()
"""


"""
pie chart(pasta grafiği) , bir bütünün parçalarını görmek için kullanıyoruz
"""
etiketler = ["python", "java","c++","javascript"]
degerler = [40 , 25 , 20 ,15]

#degerler = pasta dilimlerinin büyüklüğü
#labels = birinin etiketi
# %1.1f%% = yüzdeyi bir basamaklı olduğunu gösterir
renkler = ["orange" , "blue" , "red" , "yellow"]
ayrim = [0.1 , 0,0,0]
plt.pie(degerler , labels= etiketler ,explode = ayrim, autopct="%1.1f%%" , colors = renkler)
plt.title("Programlama Dili Kullanımı")
plt.show()

"""
scatter plot(dağilim) iki değişken arasindaki ilişkiyi göstermek için kullaniliyor
"""

calisma_saatleri = [1,2,3,4,5,6]
notlar = [50,55,60,65,70,85]

plt.scatter(calisma_saatleri , notlar, color = "red", s = 100)
plt.title("Çalışma Süresi ve Sinav Notu")
plt.show()

#birden fazla veri grubu çizdirme
x1 = [1,2,3,4,5,6]
y1 = [10,20,30,40,50,60]

x2 = [2,4,6,8,10,12]
y2 = [15,25,36,27,26,12]
plt.scatter(x1,y1, color = "blue" , label = "fen")
plt.scatter(x2,y2,color = "red" , label = "matematik")
plt.legend()
plt.show()

"""
subplots = birden fazla grafiği ayni anda gösterme
"""

x = [1,2,3,4]
y1= [10,20,30,40]
y2 = [40,30,20,10]

plt.subplot(1,2,1) #(satır , sütun , grafik numarası)
plt.plot(x,y1)
plt.title("Grafik 1")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Grafik 2")

plt.show()

#farklı grafik kullanarak da subplot oluşturulabilir