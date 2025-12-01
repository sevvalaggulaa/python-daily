import re
result=dir(re)

str="Python Kursu: Python Programlama Rehberiniz | 40 saat"

result=re.findall("Python",str) #Cümledeki tüm Python kelimelerini liste olarak bulur.
result=len(result) #Kaç tane bulduğunu sayar

result= re.split(" ",str) #Metni boşluk karakterlerinden böler
result= re.split("R",str)

result=re.sub(" ","-",str)

result=re.search("Python",str) #Sadece ilk bulduğu eşleşmeyi match objesi olarak alır.
result=result.span() # Bulduğu kelimenin başlangıç ve bitiş indeksini verir
# result=result.start()
# result=result.end()
# result=result.group()
# result=result.string()


result=re.findall("[abc]",str) # a, b veya c karakterlerinden herhangi birini ara.
result=re.findall("[sat]",str)# s, a veya t ara.
result=re.findall("[a-z]",str)# a'dan z'ye küçük harfleri ara
result=re.findall("[0-5]",str)
result=re.findall("[^abc]",str)# a, b veya c OLMAYAN her şeyi getir


result=re.findall("...",str) # Herhangi 3 karakteri getir (Nokta = Her şey)
result=re.findall("Py..on",str)

result=re.findall("^P",str)#string P ile mi başlıyor

result=re.findall("t$",str)#string t ile mi başlıyor
result=re.findall("saat$",str)

result=re.findall("sa*t",str) # s ile t arasında hiç 'a' olmayabilir veya sonsuz tane olabilir

result=re.findall("sa+t",str)# s ile t arasında en az bir tane 'a' olmalı

result=re.findall("sa?t",str) # s ile t arasında ya hiç 'a' yok ya da bir tane var

result=re.findall("a{2,3}",str) # 'a' harfi peş peşe 2 veya 3 kere tekrar ediyor mu?
result=re.findall("[0-9]{2}",str) # Rakamlar peş peşe 2 basamaklı mı?

result=re.findall("a|s",str) #a veya s harfini bul
result=re.findall("(a|s)t",str) #(a veya s) olsun, hemen arkasından t gelsin


result=re.findall(r"\APython",str) # Metnin TAM başlangıcı Python mı?
result=re.findall(r"saat\Z",str)# Metnin TAM sonu saat mi?


print(result)
