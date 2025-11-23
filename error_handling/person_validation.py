class Person:
    def __init__(self,name,year):
        if len(name) >10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name =name
            self.year = year

p = Person("sevvalsevvalsevvalsevval",2990)
