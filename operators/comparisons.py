# comparisons.py
# Karşılaştırmalar ve mantıksal operatörler

a = int(input("a: "))
b = int(input("b: "))
result = a > b
print(f"a: {a} b: {b}'den büyük mü?: {result}")

vize1 = float(input("1. vize: "))
vize2 = float(input("2. vize: "))
final = float(input("final: "))
ortalama = ((vize1 + vize2) / 2) * 0.6 + final * 0.4
print(f"Not ortalamanız: {ortalama} ve dersten geçme durumu: {ortalama >= 50}")

x = 5
hak = 5
devam = 'e'
result = 5 < x < 10
result = x > 5 and x < 10
result = hak > 0 and devam == 'e'
result = x > 0 or x % 2 == 0
result = not(x > 0)
result = (x > 5 and x < 10) and (x % 2 == 0)
print("Mantıksal sonuç:", result)

sayi = float(input("Sayı: "))
result = sayi > 0 and sayi <= 100
print(f"Sayı 0 ile 100 arasında mı? {result}")

sayi = int(input("Sayı: "))
result = sayi > 0 and sayi % 2 == 0
print(f"Pozitif çift sayı mı? {result}")

