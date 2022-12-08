print ("Pilihan Model Matematika")
1 == "Perkalian"
2 == "Pembagian"
print ("1. Perkalian")
print ("2. Pembagian")
inputan = int(input("Masukkan model matematika yang diinginkan 1/2 : "))
tabel = int(input("Menampilkan table matematika dari angka: "))
if(inputan == 1):
    for i in range(1,11):
        print(tabel, "x", i, "=", tabel*i)
elif(inputan == 2):
    for i in range(50,66):
        print(i, ":", tabel, "=", i/tabel)
else:
    if(inputan > 2):
        print("Pilihan tidak tersedia, jangan ngasal!")
