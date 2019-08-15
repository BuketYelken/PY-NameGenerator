# fonksiyon tanımlamak için def diye bir parametre kullanıyoruz, def'in yanına fonskiyon adını yazıyoruz

def selamla(isim = "isimsiz"):      #fonksiyonu tanımladık ve varsayılan bir değer gönderdik, eğer bir input girmezsek isims,z yazacak
    print("Merhaba" , isim)
    print("Nasılsın?")

selamla("Buket")   #fonksiyonu çağırdık

selamla()

def toplama(a,b,c):
    return a+b+c

toplam = toplama(3,4,5)
print(toplam)

