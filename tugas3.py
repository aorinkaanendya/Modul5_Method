def penjumlahan(a, b):
    hasil = a + b
    print("Hasil penjumlahan:", hasil)

def perkalian(a, b):
    hasil = a * b
    print("Hasil perkalian:", hasil)

def pembagian(a, b):
    if b != 0:
        hasil = a / b
        print("Hasil pembagian:", hasil)
    else:
        print("Pembagian oleh nol tidak dapat dilakukan!")

def pengurangan(a, b):
    hasil = a - b
    print("Hasil pengurangan:", hasil)

def pangkat(a, b):
    hasil = a ** b
    print("Hasil pangkat:", hasil)

def kalkulator():
    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")

    pilihan = int(input("Masukkan pilihan 1-5: "))

    if pilihan >= 1 and pilihan <= 5:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        if pilihan == 1:
            penjumlahan(angka1, angka2)
        elif pilihan == 2:
            perkalian(angka1, angka2)
        elif pilihan == 3:
            pembagian(angka1, angka2)
        elif pilihan == 4:
            pengurangan(angka1, angka2)
        elif pilihan == 5:
            pangkat(angka1, angka2)
    else:
        print("Pilihan tidak valid!")

    ulangi = input("Apakah kamu ingin mengulangi perhitungan? (y/n): ")
    if ulangi.lower() == 'y':
        kalkulator()
    else:
        print("Terima kasih telah menggunakan kalkulator sederhana ini!")

kalkulator()
