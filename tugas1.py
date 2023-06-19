def nilai(bilangan):
    if(bilangan % 2 == 0):
        print("Bilangan yang dimasukkan adalah Genap")
    else:
        print("Bilangan yang dimasukan adalah Ganjil")
        
bilangan = int(input("Masukkan bilangan: "))
nilai(bilangan)