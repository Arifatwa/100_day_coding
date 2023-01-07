print ( "NILAI MATA KULIAH PBO")

nama =input("Masukkan Nama         : ") 
uts = int(input ("Masukkan Nilai UTS    : ")) 
uas = int(input("Masukkan Nilai UAS     : ")) 
tugas = int(input("Masukkan Nilai Tugas : ")) 
print("========================================")  
print ("Nama       :" , nama ) 
print("Nilai UTS   :" , uts) 
print("Nilai UAS   :" , uas) 
print("Nilai Tugas :" , tugas)   
akhir =round(uts+uas+tugas) / 3 
print("Nilai Akhir : " , akhir)  
print("===========================================") 

if akhir >= 90 and akhir < 100 :
      print("Predikat : A ") 
      print("Keterangan : Lulus") 
elif akhir >= 60 and akhir < 90 : 
    print("Predikat : B ") 
    print("Keterangan : Lulus") 
elif akhir >= 40 and akhir < 60 : 
    print("Predikat : C ") 
    print("Keterangan : Tidak Lulus") 
elif akhir >= 30 and akhir < 40 : 
    print("Predikat : D ") 
    print("Keterangan : Tidak Lulus / kita ketemu lagi tahun depan")  
elif akhir >= 0 and akhir < 30 : 
    print("Predikat : E ") 
    print("Keterangan : Tidak Lulus / kita ketemu lagi tahun depan")  