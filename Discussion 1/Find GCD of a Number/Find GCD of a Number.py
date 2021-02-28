# MUHAMMAD AKBAR HAMID (1808561064) / KRIPTOANALISIS
# PROGRAM UNTUK MENCARI FAKTOR PERSEKUTUAN TERBESAR (FPB) (FIND GCD A NUMBER)

# Menggunakan fungsi rekursif
def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)
x =int (input ("Masukkan bilangan pertama : ")) # Menginputkan bilangan pertama
y =int (input ("Masukkan bilangan kedua : ")) # Menginputkan bilangan kedua
bil = gcd(x, y) #Memanggil gcd untuk mencari hasil
print("Faktor persekutuan terbesarnya adalah ", bil)