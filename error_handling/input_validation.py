# Kullanıcı q değerini girmedikçe alınan her inputun 
#sayı olduğundan emin olun aksi halde hata mesajı yazdırın

while True:
    sayi = input("sayi: ")
    if sayi == "q":
        break

    try:
        result=float(sayi)
        print("girdiginiz sayi: ",result)
        break
    except ValueError:
        print("geçersiz sayı")
        continue
