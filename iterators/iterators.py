liste=[1,2,3,4,5]

# MANUEL İLERLEME
iterator=iter(liste)  # Listeyi "gezilebilir" (iterator) bir nesneye dönüştürdüm.
print(next(iterator)) # İlk elemanı manuel çağırdım.
print(next(iterator)) # İmleç bir yana kaydı, sıradakini verdi.
print(next(iterator))
print(next(iterator))
print(next(iterator)) # Liste bitti. Bir daha 'next' dersem hata verir.

# OTOMATİK İLERLEME (FOR)
for i in liste: # For döngüsü; iter() ve next() işlemlerini benim yerime otomatik yapar.
    print(i)

#FOR DÖNGÜSÜNÜN ARKA PLANI
iterator= iter(liste)
while True: # For döngüsünün aslında nasıl çalıştığını manuel simüle ediyorum.
    try:
        element=next(iterator) # Sıradakini almayı dene.
    except StopIteration: # Eğer liste biterse Python hata fırlatır, hatayı yakalayıp döngüyü bitir (break).
        break

# KENDİ ITERATOR SINIFIMI YAZMA
class MyNumbers:
    def __init__(self,start,stop):
        self.start =start
        self.stop=stop
    def __iter__(self):
        return self # Bu sınıfın bir iterator olduğunu belirtiyorum (kendini döndürür).
    def __next__(self):
        if self.start <=self.stop:
            x=self.start
            self.start +=1 # Her adımda sayıyı 1 artırıp hafızada tutuyorum.
            return x
        else:
            raise StopIteration # Bitiş sayısına gelince durması için manuel hata fırlatıyorum.
            
list = MyNumbers(10,20)


myiter=iter(list)
while True:
    try:
        element=next(myiter) # Yazdığım sınıfın çalışıp çalışmadığını test ediyorum.
    except StopIteration:
        break
