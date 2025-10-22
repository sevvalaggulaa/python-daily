# Function examples

def say_hello(name="user"):
    return "Hello " + name

msg = say_hello("Şevval")
print(msg)


def total(num1, num2):
    return num1 + num2

print(total(10, 20))
print(total(15, 20))


def calculate_age(birth_year):
    return 2025 - birth_year


def years_until_retirement(birth_year, name):
    """Calculate years left until retirement (age 65)."""
    age = calculate_age(birth_year)
    retirement = 65 - age

    if retirement > 0:
        print(f"{name}, you have {retirement} years left until retirement.")
    else:
        print(f"{name}, you are already retired!")


years_until_retirement(2003, "Şevval")
years_until_retirement(1993, "Mahmut")


def add(*params):
    total = 0
    for n in params:
        total += n
    return total

print(add(10, 20, 30, 40))


def display_user(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

display_user(name="Şevval", age=22, city="Istanbul", email="sevval@gmail.com")


def my_func(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

my_func(10, 20, 30, 40, 50, key1="abc", key2="xyz")


def to_list(*params):
    return list(params)

print(to_list(10, 20, 30, "hello"))


def find_primes(sayi1, sayi2):
    """Print prime numbers between sayi1 and sayi2."""
    for number in range(sayi1, sayi2):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)

# find_primes(2, 20)


def divisors(num):
    """Return divisors of a number."""
    divisors_list = [i for i in range(2, num) if num % i == 0]
    return divisors_list

print(divisors(20))


# Lambda & map examples
numbers = [1, 2, 3, 5, 9]
squares = list(map(lambda num: num ** 2, numbers))
print(squares)


# Scope examples
name = "global string"

def greeting():
    def hello():
        name = "Ada"
        print("Hello " + name)
    hello()

greeting()


x = 50

def test():
    global x
    print(f"x before change: {x}")
    x = 100
    print(f"x after change: {x}")

test()
print(f"x outside function: {x}")


# Bank account example
hesapA = {
    "ad": "Şevval Akgül",
    "hesapNo": "627893",
    "bakiye": 700000,
    "ekHesap": 20000
}

hesapB = {
    "ad": "Akif Akgül",
    "hesapNo": "623893",
    "bakiye": 900000,
    "ekHesap": 10000
}


def bakiye_sorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL")


def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiye_sorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ek_hesap_kullan = input("Ek hesap kullanılsın mı? (e/h): ")
            if ek_hesap_kullan == "e":
                ek_miktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ek_miktar
                print("Paranızı alabilirsiniz.")
                bakiye_sorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print("Yetersiz bakiye.")
            bakiye_sorgula(hesap)


para_cek(hesapA, 710000)
print("**********")
para_cek(hesapA, 5000)

