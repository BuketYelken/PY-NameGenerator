print("Hello World")

birsayı = 5
print(birsayı)

degisken = "Buket Yelken"
print(degisken)

a = 5
b = 6

c = b + a
print(c)

print("Buket", 18, "Yelken")

print("Buket\nYelken")

print("01","01","2001", sep = "/") ### biraz önemli bence unutma bunu

print(" {} + {} = {}".format(2,3,2+3))  # süslü parantez formatıyla yanına yazdığımız şeyleri içine attık gibi şeyler

"""
yorum satırları

"""

a = 3
b =3.14
c = "Python"
d = [1,2,3,4,5, "python"]
e = (1,2,3,4,5, "python")
f = {"Elma": 3 , "Armut": 4, "Kiraz": 5}
g = False # boolean tipi veri tipi

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print(a,b,c,d,e,f,g)

print (3+4)
print(10-3)
print(10*3)
print(10/4)
print (10//4) # bölümden çıkan tam kısmı göster
print(10%4) # bölümden sonraki kalanı göster

x = "python "
y = "programlama "
z = "dili "
w = x + y + z # stringleri toplayabiliyorsun

print(w)

print(x*5) # x de yazan stringi 5 kere ekrana yazar yan yana

h = "Python"
i = [1,2,3,4,5,6,7]
print(h[0])
print(i[2])
print(len(h))  # len fonksiyonu a dizisinin kaç elemanı olduğunu çıktı veriyor
print(h[len(h)-1]) #stringin içindeki son elemanı bastırır

print(h[0:2]) # 0.indeksten başla 2.indekse kadar git
print(h[3: ]) # 3.indeksten başla sonuna kadar git
print(h[::2]) # baştan başlayıp sona kadar 2şer 2şer git


# SÖZLÜK TANIMLICAZ

k= {"Elma": 3, "Armut":4, "Kiraz":5}
print(k["Elma"])
print(k["Armut"])
print(k["Kiraz"])

# KULLANICIDAN INPUT ALMAK

l = int(input("l:"))
m = int(input ("m:"))
n = int(input("n:"))
print("Toplam",l+m+n)

# KOŞUL DURUMU

yas = int(input("Yaşınızı giriniz: "))
print("Yaşınız",yas)
print(yas, "yaşındasınız")

if yas < 18:
    print("Reşit değilsiniz. Mekana giremezsiniz!")
else:
    print("Hoş geldiniz...")


"""
karşılaşstırma oparetörleri
<
>
<=
>=
==
!=
"""

islem = int(input("İşlemi giriniz: "))

if islem == 1:
    print("İşlem 1'i seçtiniz")
elif islem == 2:
    print("İşlem 2'yi seçtiniz")
elif islem == 3:
     print("İşlem 3'ü seçtiniz")
else :
    print("Yanlış numara tuşladınız")


# MANTIKSAL BAĞLAÇLAR

p = int(input("Sayı giriniz: "))
r = int(input("Sayı giriniz: "))

if p==5 and r == 9: # and yerine or operatörü de kullanabilirsin
    print("Well done...")
else:
    print("Yanlış sayı tuşladınız")


if (not (3==4)): # if in içindeki önerme true ise false yapıyor, false ise true yapıyor
    print ("Sayılar eşit değil")
