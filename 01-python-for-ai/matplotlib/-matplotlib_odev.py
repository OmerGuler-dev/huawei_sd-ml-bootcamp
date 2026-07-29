import matplotlib.pyplot as plt

aylar = ["ocak","şubat","mart","nisan","mayis","haziran"]
satislar = [120 ,150,170,160,200,220]
karlar = [20,35,40,30,50,60]
reklam = [5,8,10,7,12,15]


plt.plot(aylar, satislar , color = "red" , marker = "o")
plt.title("Aylara Göre Satişlar")
plt.xlabel("Aylar")
plt.ylabel("satislar")
plt.show()


plt.bar(aylar,reklam , color ="green")
plt.title("Aylara Göre Reklam Grafiği")
plt.xlabel("aylar")
plt.ylabel("reklam")
plt.show()

plt.pie(satislar, labels=aylar,autopct="%1.1f%%")
plt.title("Aylara göre satış dağılımı")
plt.axis("equal")
plt.show()

plt.subplot(1,2,1)
plt.plot(aylar ,satislar,marker = "o")
plt.title("SAtışlar")

plt.subplot(1,2,2)#satır , sütun , grafik numarası
plt.bar(aylar,reklam, color = "orange")
plt.title("Aylara Göre Reklamlar")
plt.show()


