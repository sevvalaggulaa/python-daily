# Liste elemanları içindeki sayısal değerleri bul

liste = [1,2,"5a","10b","abc","10","50"]
for x in liste:
    try:
        result= int(x)
        print(result)
    except ValueError:
        continue
