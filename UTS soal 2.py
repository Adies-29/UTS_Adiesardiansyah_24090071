tahun = int(input("Masukan Tahun : "))
if tahun / 400:
    if tahun / 4 and tahun % 100:
        print(f"Tahun {tahun} merupakan Tahun Kabisat")
    else:
        print("bukan kabisat")
else:
    print("Bukan kabisat")        

       

  
    