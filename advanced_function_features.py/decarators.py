def my_decarator(func):
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper



@my_decarator
def sayHello():
    print("hello")

@my_decarator
def sayGreeting():
    print("greeting")

# sayHello = my_decarator(sayHello)
# sayGreeting = my_decarator(sayGreeting)

sayHello()
sayGreeting()




import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " +func.__name__ +" "+ str(finish - start)+ " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))  

@calculate_time
def toplama(a,b):
    print(a + b)

usalma(2,3)
faktoriyel(6)
