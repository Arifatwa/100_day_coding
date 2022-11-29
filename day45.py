nomor_Ruko = int(input('Masukkan nomor Ruko Anda: '))
if nomor_Ruko >= 50:
   print('nomor Ruko benar')
elif nomor_Ruko >= 40:
    print('nomor Ruko kurang tepat')
if nomor_Ruko >= 30:
    print('nomor Ruko tidak di temukan')
else:
    print(' Nomor Ruko salah')


print('=====================================')

i = 2
batas = 3

if i  < batas:
   iDua = i + 1
   if iDua < batas:
      iTiga = iDua + 1
      if iTiga < batas:
         iEmpat = iDua + 1
         if iEmpat < batas:
            iLima = iDua + 1
            if iLima < batas:
               iEnam = iDua + 1
               print(iEnam)
            print(iLima)
         print(iEmpat)
      print(iTiga)
   print(iDua)
print(i)