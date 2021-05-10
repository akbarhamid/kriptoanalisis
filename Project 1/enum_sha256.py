import sys
import hashlib

def hash_enum():
    #init i dan j
    i = 1
    j = 1
    unichr = chr  # untuk python versi 3.x
    while i <= 26:
        while j <= 26:
            my_enum = unichr(i+96) + unichr(j+96) # ubah angka menjadi karakter unicode
            my_string = my_enum  # def string sebagai enum char
            string_hash = hashlib.sha256(my_string.encode()).hexdigest()  # hash string dengan SHA256
            print(my_enum, "--", string_hash)  # print hash setiap enum char
            j += 1
        print("----------------------------------------------------------------------")
        j = 1
        i += 1

def simpan_database():
    conf = input("Simpan Hash ke Database [y/n]? ")  # konfirmasi untuk menyimpan
    if conf.lower() in ['y', 'Y', 'yes']:
        original_stdout = sys.stdout # menyimpan hasil hash dan enum kedalam database
        with open('database.txt', 'w') as file:
            sys.stdout = file
            print('\n======================================================================')
            print('CHR --                        HASH SHA256')
            print('======================================================================')
            print(hash_enum())
            sys.stdout = original_stdout # reset standard output
        print('\nHash Berhasil Di Simpan!')
    elif conf.lower() in ['n', 'N', 'no']:
        print('\nHash Tidak Disimpan!')

def baca_database():
    string_file = open("database.txt", "r") # baca hash dari database.txt
    string = string_file.read() # isi string dengan input data dari database.txt
    return string