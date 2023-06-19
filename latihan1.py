#MENGGUNAKAN METHOD FUNCTION
def keliling_persegi(sisi):
    hasil = 4*sisi
    return hasil

def luas_persegi(sisi):
    hasil = sisi*sisi
    return hasil

sisi = int(input("Masukkan sisi: "))
print("Keliling persegi adalah: %d" %keliling_persegi(sisi))
print("Luas persegi adalah: %d" %luas_persegi(sisi))

