class Person:
    #class attributes
    address= "no information"
    #constructor (yapıcı metod)
    def __init__(self, name, year):
    #object attributes
        self.name=name
        self.birthyear=year
        print("init komutu calisti")
    # instance methods
    def intro(self):
        print("hello there. I am "+ self.name)
    
    def calculateAge(self):
        return 2025 - self.year

#object (instance)
p1 = Person(name='ali',year= 1990)
p2 = Person(name='yagmur',year= 1997)

p1.intro()
p2.intro()

print(f"adim: {p1.name} ve yasim: {p1.calculateAge}")
print(f"adim: {p2.name} ve yasim: {p2.calculateAge}")

#updating
p1.name="ahmet"
p1.address="kocaeli"

#accessing object attributes
print(f'name: {p1.name} year: {p1.birthyear} address: {p1.address}')
print(f'name: {p2.name} year: {p2.birthyear} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)
