# variables_and_math.py
# Değişken atamaları, tuple unpacking ve matematiksel işlemler

# Değişken atamaları ve tuple unpacking
x, y, z = 5, 10, 20
x, y = y, z
print("x, y, z:", x, y, z)

values = 1, 2, 3
print("values:", values, type(values))
x, y, z = values

# Matematiksel işlemler
x, y, z = 2, 5, 10
numbers = [1, 5, 7, 10, 6]

a = int(input("1. sayı: "))
b = int(input("2. sayı: "))
result = (a * b) - (x + y + z)
print("Sonuç:", result)

result = y // x
print("y // x:", result)

result = (x + y + z) % 3
print("(x+y+z) % 3:", result)

result = y ** x
print("y ** x:", result)

x, *y, z = numbers
result = z ** 3
print("z ** 3:", result)

