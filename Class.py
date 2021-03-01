class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="Lenovo"
            self.processor="I7"
            self.price=1000000
        def show(self):
            print(self.brand,self.processor,self.price)
s1=Student("DEVESH",1)
s2=Student("PRASAD",2)
