def kerucut(rk):
 return 1/3*22/7*rk**2*t
def bola (r):
 return 4/3*22/7*r**3
if __name__ == "__main__":

 print("Menghitung Volume Kerucut dalam Bola \n")

r = int(input("Masukkan jari-jari bola: "))
rk = int(input("Masukkan jari-jari alas kerucut: "))
t = int(input("Masukkan tinggi kerucut: "))

# variable
a = kerucut(rk)
b = bola (r)


print("\n")

print("Volume kerucut adalah = {}".format(a))
print("Volume bola adalah = {}".format(b))