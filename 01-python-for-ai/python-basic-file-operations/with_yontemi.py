with open("ornek.txt" , "r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)
    #otomatik şekilde kendi kendine kapanıyor

    #daha temiz bir kod

with open("with_ile_yazma.txt" , "w" , encoding= "utf-8") as dosya2:
    dosya2.write("with ile yazma islemi")
