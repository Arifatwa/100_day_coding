print("======================Mencari nilai Maksimal=======================")
print("nilai maksimum")
a =[11,45,7,89,10,12,34,6,7,9]
nilai = max(a)
print(nilai)
a.sort()
print(a)

#Mencarai nilai maksimum dengan cara panjang
b= [11,45,7,89,10,12,34,6,7,9]
hasil=b[0]
for i in range (1,len(b)):
   x = b[i]
   if x<=hasil:
       hasil=x
print("nilai maksimal:",hasil)

print("==============mencari nilai minimum=============")

#nilai minimum
b =[11,45,7,89,10,12,34,6,7,9]
nilai = min(b)
print(nilai)
#mencari nilai minimum dengan cara panjang 
print("nilai minimum")
b = [11,45,7,89,10,12,34,6,7,9]
hasil =b[0]
for i in range (1,len(b)):
    x = b[i]
    if x<=hasil:
        hasil=x
print("nilai minimum:",hasil)
