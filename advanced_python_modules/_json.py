import json

person_string='{"name":"Ali","languages":["python","C#"]}' # bu dışarıdan gelen string veri (JSON string)
person_dict={"name":"Ali","languages":["Python","C^"]} # normal python sözlüğü (dictionary)

# 1. string -> dict (loads: sonunda 's' var, yani STRING için)
result=json.loads(person_string) # stringi aldık, sözlüğe çevirdik. 
print(result["name"])
print(result["languages"])
print(result)

# 2. dosya -> dict (load: sonunda 's' YOK, dosya okuyoruz)
with open("person.json") as f:
    data=json.load(f) # dosyadan okuyup direkt sözlüğe çeviriyor.
    print(data["name"])
    print(data["languages"])

    
# 3. dict -> string (dumps: yine 's' var, stringe dönüştür)
result=json.dumps(person_dict) # sözlüğü paketleyip string yaptık. Başka programa yollamak için.
print(result)
print(type(result)) # tipi artık 'str' oldu.

# 4. dict -> dosya (dump: 's' yok, direkt dosyaya yaz)
with open("person.json","w") as f:
    json.dump(person_dict, f) # sözlüğü alıp direkt dosyanın içine basıyor.

# Çıktıyı Güzelleştirme
person_dict=json.loads(person_string)
result=json.dumps(person_dict,indent=4,sort_keys=True) # indent=4: girintili yaz, sort_keys: alfabetik sırala.
print(person_dict) # karışık duran
print(result) # okunaklı duran
