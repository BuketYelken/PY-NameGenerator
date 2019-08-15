file = open("dosya.txt", "w") # file değişkenine atıyoruz, open ile dosyayı açıyoruz
# parantez içine dosya adını ve yanına açmak istediğimiz formatı yazıyoruz
# w kipi dosyayı her seferinde yeniden oluşturup öncekileri siliyor
file.write("Dosyanın içine bir şeyler yazdık")

file.close()

file = open("dosya.txt", "a")

file.write("\nNaber Python\n")
file.write("Naber Java\n")
file.write("Naber C++")

file.close()

file = open("dosya.txt", "r")

veri = file.read() # dosya içini okuyup veri diye bir değişkene attık
print(veri)   # ve bunu ekrana bastırdık

file.close()


file = open("dosya.txt", "r")

veri = file.read(10) # dosyanın başından başlayarak 10 karakter okuyor, file by haliyle dosyanın başında bulunuyor
print(veri)   # ve bunu ekrana bastırdık

file.close()

file = open("dosya.txt", "r")
file.seek(36)  # file değişkeni dosyanın içindeki 36.karakteri gösteriyor
veri2 = file.read(10) # dosyanın 36.karakterinden itibaren 10 karakter oku
print(veri2)    # ve bunu ekrana yazdır

file.close()



file = open("dosya.txt", "r")

for satir in file:   # dosyanın içini satır satır okuduk ama tam anlamadım sanki bu işlemi ???????
    print(satir)
file.close()

