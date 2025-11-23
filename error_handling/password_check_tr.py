# Girilen parola içinde türkçe karakter hatası veriniz
def checkPassword(parola):
    turkce_karakterler="şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeriyor")
        else:
            pass

    print("geçerli parola")

parola = input("parola: ")
try:
    checkPassword(parola)
except TypeError as error:
    print(error)
