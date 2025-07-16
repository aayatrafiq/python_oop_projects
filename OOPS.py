class Student:
    def __init__(self, name, math, phy, chem):
        self.name = name
        self.math = math
        self.phy = phy 
        self.chem = chem

    def average(self):
        avg = (self.math + self.phy + self.chem )/3
        return avg
    
    @staticmethod
    def hello():
        print("hello")

    @staticmethod
    def grade(avg): #   Here we have to pass average because we have to tell the fucn to take avg variable for garding
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        else:
            return "C"

s1 = Student("Aayat", 99, 88, 92)
avg = s1.average()
print(f"Average: {avg:.2f}, Grade: {Student.grade(avg)}")


class Car:
    def __init__(self):
        self.acc = False
        self.brake= False
        self.cluth = False
    def start(self):
        self.acc = True
        self.cluth = True
        print("Car is Starting")

car1=Car()
car1.start() #Here the unncessary steps are hidden of true etc 
#This is called Abstraction 

class Account:
    def __init__(self, balance, acc_no):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self, debit):
        self.balance -= debit
       
        print(debit, "was debited. New balance", self.balance)
    def credit(self, credit):
        self.balance += credit
        print(credit, "was credited. New balance", self.balance)
    def getbalance(self):
        return self.balance
acc1 = Account(10000, 12345)
acc1.debit(100)
acc1.credit(200)
print(acc1.getbalance())