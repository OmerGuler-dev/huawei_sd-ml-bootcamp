with open("notlar.txt" , "w", encoding="utf-8") as dosya:
    dosya.write("25\n80\n90\n100\n85")


notlar = []

with open("notlar.txt" , "r" , encoding= "utf-8") as dosya2:
    for satir in dosya2:
        notlar.append(int(satir.strip()))

print(notlar)

ortalama = sum(notlar) / len(notlar)
en_yuksek = max(notlar)
en_dusuk = min(notlar)

print(f"ortalama = {ortalama} , en yüksek = {en_yuksek} , en düşük = {en_dusuk}")


with open("sonuc.txt" , "w", encoding="utf-8") as dosya3:
    for i in notlar:
        if i > 50:
            dosya3.write("Sinifi geçti\n")
        else:
            dosya3.write("Sinifta kaldi\n")
