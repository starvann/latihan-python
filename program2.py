print("=== MENGHITUNG LUAS BANGUN DATAR ===")
print("1. Luas Persegi")
ps = int(input("Masukkan Panjang Sisi Persegi: "))
lp = ps * ps
print("Luas Persegi = ", ps, "x", ps, "=", lp)

print("2. Luas Persegi Panjang")
ppp = int(input("Masukkan Panjang Persegi Panjang: "))
lebpp = int(input("Masukkan Lebar Persegi Panjang: "))
lpp = ppp * lebpp
print("Luas Persegi Panjang = ", ppp, "x", lebpp, "=", lpp)

print("3. Luas Segitiga")
als = int(input("Masukkan Alas Segitiga: "))
ts = int(input("Masukkan Tinggi Segitiga: "))
ls = 0.5 * als * ts
print("Luas Segitiga = 0.5 x ", als, "x", ts, "=", ls)

print("4. Luas Lingkaran")
r = int(input("Masukkan Jari-Jari: "))
ll = 3,14 * r * r
print("Luas Segitiga = 3,14 x ", r, "x", r, "=", ll)

print("5. Luas Jajar Genjang")
alsj = int(input("Masukkan Alas Jajar Genjang: "))
tj = int(input("Masukkan Tinggi Jajar Genjang: "))
lj = 0.5 * alsj * tj
print("Luas Jajar Genjang = ", alsj, "x", tj, "=", lj)

print("3. Luas Trapesium")
alsa = int(input("Masukkan Alas a Trapesium: "))
alsb = int(input("Masukkan Alas b Trapesium: "))
tst = int(input("Masukkan Tinggi Trapesium: "))
ls = 0.5 * (alsa + alsb) * tst 
print("Luas Trapesium =  0.5 x (", alsa, "+", alsb, ") x", tst ) 