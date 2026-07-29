"""
Class =
    bir nesnenin nasıl olacağını tanımlayan bir şablondur
    taslak ya da plan gibi
    kodun daha düzenli durması ve kod tekrarini azaltir
    yönetimi kolaylaştırır

    __init__ metodu
    attribute ve metod
    object oluşturma 
"""

class Ogrenci :
    def __init__(self, isim , yas ): #self oluşturulan nesneyi temsil eder , isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor : isim = {isim} , yaş = {yas}")
        
#nesne(object) oluşturma
ogrenci1 = Ogrenci("Ali",21)

"""
Attribute bir class veya a nesnesine ait özellikleri temsil eden değişkenlerdir
-yani bir nesnenin verilerini tutan yapilardir 
Öğrenci : 
        -isim
        -yaş
        -bölüm
        (Bunlar öğrencinin attributelaridir)
"""

class Ogrenci:

    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas #bu bölümlerde self kullanılmasını nedeni bunun nesneye ait olduğunu göstermek için


#attribute kullanımı
ogrenci1 = Ogrenci("Ahmet" , 25)
print(ogrenci1.yas)
print(ogrenci1.isim)

"""
Metotlar = bir class içerisinde tanimlanann fonksiyonlardir
Bir nesnenin yapabileceği işlemleri temsil ederler
"""
class Ogrenci:
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Merhaba benim adim {self.isim} , {self.yas} yaşindayim")


ogrenci1 = Ogrenci("Ahmet" , 25)
ogrenci2 = Ogrenci("Omer" , 30)

ogrenci1.tanit()
ogrenci2.tanit()

"""
#object oluşturma ve class kullanimi
    class = şablon
    object(nesne) = şablondan üretilen yapidir


"""
class Kitap:
    def __init__(self,ad, yazar , sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def bilgiGoster(self):
        print(f"Kitap adi {self.ad}, yazar = {self.yazar} , sayfa = {self.sayfa}")


kitap1 = Kitap("Yeraltindan Notlar" , "Dostoyevski" , 500)

#attribute değerlerine erişim =
print(kitap1.ad)
print(kitap1.sayfa)

#method 
kitap1.bilgiGoster()

#birden fazla obje oluşturma 
kitap1 = Kitap("Yeraltindan Notlar" , "Dostoyevski" , 500)
kitap2 = Kitap("Suç Ve Ceza" , "Dostoyevski" , 1000)
kitap3 = Kitap("Karamazov Kardeşler" , "Dostoyevski" , 700)

kitap3.bilgiGoster()
#class kullanmanın en büyük avantajı aynı yapıyı tekrar tekrar kullanmaktır
