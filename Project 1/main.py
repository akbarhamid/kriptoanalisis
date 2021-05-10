from enum_sha256 import hash_enum, simpan_database, baca_database  # import modeul

def main():
    print('PROGRAM MEMBUAT ENUMERASI DAN MENGGABUNGKAN SHA256')
    print('Kelompok Diskusi 4/D: 1808561012 - Sang Putu Febri Wira Pratama | 1808561064 - Muhammad Akbar Hamid\n')
    print('MENU')
    print("1. Buat Enumerasi Hash SHA256")
    print("2. Lihat Database")
    menu = int(input("\nPilih Menu : "))
    if menu == 1:
        hash_enum()
        simpan_database()
    elif menu == 2:
        string = baca_database()
        print(string)
    else:
        print("\nPilihan Tidak Ada!")

main()
