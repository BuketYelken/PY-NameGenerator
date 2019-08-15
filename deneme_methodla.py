kardiz1 = "deneme"
print(kardiz1.replace("e", "E", 2))

kardiz = input("Kurum adını giriniz: ")

for i in kardiz.split():
    print(i[0], end="")


kardiz2 = "Ankara, İstanbul, Kayseri, Zonguldak, Manisa, Çanakkale, Ordu"

for i in kardiz2.split(","):
    print(i)

kardiz3 = "Buket isimli öğrenci Buket Yelken Gazi Üniversitesinde Buket adlı öğrenci Buket Yelken isimli öğrencinin numarası sistemde öğrencinin yok"

for i in kardiz3.split("öğrenci"):
    print(i)