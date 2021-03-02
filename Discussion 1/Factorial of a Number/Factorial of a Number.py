# MUHAMMAD AKBAR HAMID (1808561064) / KRIPTOANALISIS
# PROGRAM UNTUK MENCARI BILANGAN FAKTORIAL (FACTORIAL OF A NUMBER)

def faktorial(bil):
    # Fungsi rekursif yang memanggil sendiri untuk mencari faktorial dari bilangan
    if bil == 1:
        return bil
    else:
        return bil * faktorial(bil - 1)
# Menginput bilangan faktorial yang akan di cari
bil = int(input("Masukkan bilangan : "))
# if bilangan inputan adalah bilangan negatif maka akan keluar pesan eror
# elif bilangan inputannya adalah 0 maka outputnya adalah 1
# else menghitung faktorial dengan memanggil fungsi yang telah diinputkan
if bil < 0:
    print("Bilangan faktorial yang cari tidak boleh bilangan negatif")
elif bil == 0:
    print("Faktorial dari 0 adalah 1")
else:
    print("Faktorial dari", bil, "adalah", faktorial(bil))
