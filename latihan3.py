def nilai(nilai1, nilai2):
    if(nilai1>nilai2):
        print(nilai1)
    elif(nilai1==nilai2):
        print("Tidak ada yang lebih besar")
    else:
        print(nilai2)
        
bil1 = int(input("Masukkan bilangan 1: "))
bil2 = int(input("Masukkan bilangan 2: "))
print("Bilangan yang lebih besar adalah: ")
nilai(bil1, bil2)