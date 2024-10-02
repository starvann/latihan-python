#konfersi suhu
print("Masukkan suhu derajat:")
c = float(input())
print("""Pilih konfersi suhu menggunakan angka:
      1. F
      2. R
      3. K
      """)
pilihan = int(input())
if pilihan == 1:
    f = 9 / 5 * c + 32
    print("Hasil dari konfersi suhu celius ke fahrenheit adalah", f)
elif pilihan == 2 :
    r = 4 / 5 * c 
    print("Hasil dari konfersi suhu celcius ke reamur adalah", r)
elif pilihan == 3:
    k = c + 275.13
    print("Hasil dari konfersi suhu celcius ke kelvin adalah", k)
else:
    print("Masukkan jawaban yang tertera pada pilihan saja!")
