# matriks 3x3
x = [[0,0,0],
     [0,0,0],
     [0,0,0]]

#input user
for i in range(len(x)):
    for j in range(len(x)):
        x[i][j] = int(input(f"Masukkan Nilai Matriks {i+1}, {j+1}: "))

#output matriks 3x3
print("Matriks: ")
for h in x:
    print(h)
    
#kalkulasi matriks ordo 3x3
y = ((x[0][0]*x[1][1]*x[2][2]) + (x[0][1]*x[1][2]*x[2][0]) + (x[0][2]*x[1][0]*x[2][1]))
z = ((x[2][0]*x[1][1]*x[0][2]) + (x[2][1]*x[1][2]*x[0][0]) + (x[2][2]*x[1][0]*x[0][1]))
hasil= y - z

#output
print(f"Hasil Matriks 3x3 adalah: {hasil}")