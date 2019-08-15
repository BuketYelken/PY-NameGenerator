liste = [1,2,3,4,5,6]
a = "araba"

print(a.startswith("ar")) # a stringi ar ile başlıyor mu diye true ya da false değeri döndürüyor
print(a.endswith("ba"))

a = a.replace("a", "o") # a karakterlerini o ya çevir
print(a)

liste.append("Pyhon") # sonuna python elemanını ekliyor
print(liste)

liste.pop() #içine hiçbir şey yazmazsan son elemanı listeden çıkarıyor
print(liste)

liste.pop(0) # 0.indeksi atıyor
print(liste)

