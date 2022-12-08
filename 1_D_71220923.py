print("Susu     = Rp20.000")
print("Permen   = Rp500")
print("roti     = Rp15.000")
print("indomie  = Rp3.000")
print("vitamin  = Rp50.000")

uang = int(input("Masukan Jumlah uang: Rp"))
mulai = input("Ketik 'START' untuk memulai: ")

Susu = 20000
Permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

if mulai.upper() == 'START':
    while True:
        beli = input("Apa barang yang akan beli?")
        if beli.upper() =='SUSU':
            if uang >= Susu:
                uang -= Susu
                print('sisa',uang)
            else:
                print(' Uang tidak cukup')
        elif beli.upper() =='ROTI':
            if uang >= roti:
                uang -= roti
                print('sisa',uang)
            else:
                print(' Uang tidak cukup')
        elif beli.upper() =='PERMEN':
            if uang >= Permen:
                uang -= Permen
                print('sisa',uang)
            else:
                print(' Uang tidak cukup')
        elif beli.upper() =='VITAMIN':
            if uang >= vitamin:
                uang -= vitamin
                print('sisa',uang)
            else:
                print(' Uang tidak cukup')
        elif beli.upper() =='INDOMIE':
            if uang >= indomie:
                uang -= indomie
                print('sisa',uang)
            else:
                print(' Uang tidak cukup')
        elif beli.lower() == 'sudah':
            break
        else:
            print('barang tidak ada')
