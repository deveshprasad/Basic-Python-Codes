class Car():
    def __init__(self,name,price,mileage):
        self.name=name
        self.price=price
        self.mileage=mileage
    def price_inc(self):
        self.price=int(self.price*1.15)
        
HONDA=Car('abc',10000,26367)
TATA=Car('xyz',12344,8779)
HONDA.CC=1500
print(HONDA.__dict__)
HONDA.price_inc()
print(HONDA.price)

