bb = int(input("Masukan Berat Badan (Kg) : "))
tb = float(input("Masukan Tinggi Badan (M) : "))

print(f"Berat badan Anda : {bb}")
print(f"Tinggi Badan Anda : {tb}")

hitung_BMI = bb/tb ** 2
bmi = hitung_BMI
print(f"Nilai BMI Anda : {bmi}")

if bmi < 18.5:
    kt= ("Berat Badan Kurang")
elif 18.5 <= bmi < 24.9:
    kt= ("Berat Badan Normal")
elif 25 <= bmi < 29.9:
    kt = ("Kelebihan Berat badan")
else:
    kt = ("Obesitas")   

print(f"Kategori Anda : {kt}")


  