def keliling_lingkaran(jari):
    hasil = 2 * 3.14 * jari
    return hasil

def luas_lingkaran(jari):
    hasil = 3.14 * jari * jari
    return hasil

jari = int(input("Masukkan jari-jari: "))
print("Keliling lingkaran adalah: %f" %keliling_lingkaran(jari))
print("Luas lingkaran adalah: %f" %luas_lingkaran(jari))