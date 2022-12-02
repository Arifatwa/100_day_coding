pin_1 = 12345678
saldo = 10000000
pin = int(input("Masukkan Pin Anda : "))

if pin == pin_1 :
    print(f"1. Penyetoran\n2. Penarikan\n3. Saldo ")
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1:
        setor = int(input('Silahkan masukkan uang : '))
        print(f'Sisa saldo anda {saldo + setor}')
    elif pilihan == 2:
        tarik = int(input("Masukkan jumlah uang yang akan di tarik : "))
        if tarik > saldo :
            print('Maaf saldo anda tidak cukup...')
        else :
            print(f'Sisa saldo anda {saldo - tarik}')
    elif pilihan == 3 :
        print(f"Sisa saldo anda : {saldo}")
else :
    print("Pin Anda Salah...")