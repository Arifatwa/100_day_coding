def calc_BT(berat, tinggi):
    BT = berat / tinggi * tinggi
    if BT > 23.7:
        return "Overweight"
    elif BT < 17.4:
        return "Underweight"
    else:
        return "Normal"
berat = float(input("Masukan berat badan dalam satuan kg: "))
tinggi = float(input("Masukan Tinggi badan dalam satuan M :"))

result = calc_BT(berat, tinggi)
print("status BT anda adalah :", result)