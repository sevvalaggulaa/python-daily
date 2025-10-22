# for loops
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

names = ["a", "b", "x"]
for name in names:
    print(f"My name is {name}")

name = "Şevval"
for n in name:
    print(n)

tuples = [(1, 2), (3, 4, 5)]
for t in tuples:
    print(t)

d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d.items():
    print(key, value)


# while loops
x = 0
while x < 10:
    if x % 2 == 0:
        print(f"Sayı çift: {x}")
    else:
        print(f"Sayı tek: {x}")
    x += 1

# example: input loop
name = ""
while not name.strip():
    name = input("İsminizi girin: ")
print(f"Merhaba {name}")


# numbers with while
numbers = [1, 3, 5, 7, 9, 12, 19, 21]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# counting backwards
i = 100
while i > 0:
    print(i)
    i -= 1


# example: add user input to list
numbers = []
i = 0
while i < 5:
    num = int(input("Sayı: "))
    numbers.append(num)
    i += 1
numbers.sort()
print(numbers)


# example: product list
products = []
adet = int(input("Kaç ürün eklemek istiyorsunuz: "))
i = 0
while i < adet:
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    products.append({"name": name, "price": price})
    i += 1

for urun in products:
    print(f"Ürün adı: {urun['name']}, fiyatı: {urun['price']}")


# continue and range examples
for letter in "Sadık Turan":
    if letter == "ı":
        continue
    print(letter)

for item in range(50, 100, 20):
    print(item)

print(list(range(5, 100, 10)))


# enumerate & zip
greeting = "hello there"
for index, letter in enumerate(greeting):
    print(index, letter)

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300, 400, 500]

for a, b, c in zip(list1, list2, list3):
    print(a, b, c)


# list comprehensions
numbers = [x for x in range(10)]
print(numbers)

squares = [x ** 2 for x in range(10)]
print(squares)

div_by_3 = [x for x in range(10) if x % 3 == 0]
print(div_by_3)

years = [1928, 1987, 2003, 2017, 2019]
ages = [2025 - year for year in years]
print(ages)

result = [x if x % 2 == 0 else "tek" for x in range(1, 10)]
print(result)

pairs = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(pairs)


# number guessing game
import random

number = random.randint(1, 50)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if number == tahmin:
        print(f"Tebrikler {sayac}. seferde bildiniz. Toplam puanınız: {100 - (100 / can) * (sayac - 1)}")
        break
    elif number > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {number}")


# check if number is prime
sayi = int(input("Sayı: "))
asal_mi = True

if sayi == 1:
    print("1 sayısı asal değildir.")
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False
            break

    if asal_mi:
        print("Asal")
    else:
        print("Asal değil")

