"""
Veri Analizi Araci
        -sayi listesi tutma
        -bu sayilarin toplamini hesapla
        -ortalamasini bul
        -en büyük ve en küçük değeri hesapla
"""
class VeriAnalizi():
    def __init__(self , veriler):#burada tek bir veri istiyoruz demek oluyor bu yüzden verdiğimiz veri liste içinde tek bir veri olması lazım
        self.veriler = veriler #attribute

    def verilerigoster(self):
        print(f"Veriler = {self.veriler}")

    def toplam(self):
        toplam = sum(self.veriler)
        print(f"toplam = {toplam}")

    def ortalama(self):
        ortalama = sum(self.veriler) / len(self.veriler)
        print(f"Ortalam = {ortalama}")
    def max_min(self):
        print(f"Maksimum değer = {max(self.veriler)} , Minimum = {min(self.veriler)}")

    def analizet(self):
        self.verilerigoster()
        self.toplam()
        self.ortalama()
        self.max_min()


verilerim = VeriAnalizi([1,2,3,4,5,6])

verilerim.analizet()

