# list_and_string.py
# Liste ve string işlemleri

# Liste işlemleri
x = [1,2,3]
y = [2,4]
del x[2]
y[1] = 1
y.reverse()
print("x == y:", x == y)
print("x is not y:", x is not y)

x = ["apple", "banana"]
print("'banana' listede mi?", "banana" in x)

# String işlemleri
name = "şevval"
print("'a ' stringde mi?", "a " in name)
print("'a' stringde yok mu?", "a" not in name)

