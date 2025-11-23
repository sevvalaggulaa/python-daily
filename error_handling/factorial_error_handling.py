# Faktoriyel fonksiyonu oluştur ve fonk gelen değerler için 
#hata mesajı verin

def factoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError("negatif değer")
    result=1
    for i in range(1, x+1):
        result *=i
    return result


for x in [5,10,20,-3,"10a"]:
    try:
        y = factoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
