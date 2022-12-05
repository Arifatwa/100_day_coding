n = int(input("N = "))
for baris in range(1, n + 1):
    for kolom in range(1, n + 1):
        print('', baris * kolom, end = '')
    print()