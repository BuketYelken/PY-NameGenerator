i = 0

while (i < 10):
    print("i:" , i)
    i += 1 # i = i +1 demek

j = 1

while (j < 1000):
    print("j:" , j)
    j *= 2



a = 0

while (a < 10): # döngü şartı doğru olsa bile break sağlandığında döngüyü kırar
    if a == 5:
        break
    print("a:" , a)
    a += 1



b = 0

while ( b < 10):
    if b == 3 or b == 5:
        b += 1
        continue  # alttakini çalıştırmayıp döngüyü başa çeviriyor
    print("b:", b)
    b += 1


