class Account:
    def __init__(self):
        self.owner = input("enter your name : ")
        self.balance = int(input("Enter your balance: "))

    def deposit(self, ammount):
        self.balance += ammount
        print (self.balance)
    def withdraw(self,ammount):
        if  ammount>self.balance:
            self.balance -=ammount
            print (self.balance)
        else:
            print("Your balance is low")
obj=Account()
obj.deposit(500)
obj.withdraw(700)