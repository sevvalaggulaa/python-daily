class Circle:
    #Class object attribute
    pi=3.14
    def __init__(self, yaricap=1):
        self.yaricap=yaricap
    
    #Methods
    def cevre_hesapla(self):
        return 2*self.pi *self.yaricap
    
    def alan_hesapla(self):
        return self.pi* (self.yaricap**2)
    
c1 =Circle()
c2=Circle(4)

print(f"c1: alan={c1.alan_hesapla()} c1: cevre= {c1.cevre_hesapla()}")
print(f"c2: alan={c2.alan_hesapla()} c2: cevre= {c2.cevre_hesapla()}")

