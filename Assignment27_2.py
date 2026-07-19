
class BankAccount():
    ROI = 10.5

    def __init__(self, Name, iniAmount):
        self.Name = Name 
        self.Balance = iniAmount 

    def Deposit(self):
        print("-------Deposit Balance--------------")
        print(f"{self.Name} Current balance is : {self.Balance}")
        self.AmtDpst = int(input("Enter Amount to Deposit : "))
        self.Balance = self.Balance + self.AmtDpst 
        print(f"User account name is :{self.Name} After Deposit balance is : {self.Balance}")

    def Withdraw(self):
        print("-------Withraw Balance--------------")
        print(f"{self.Name} Current balance is : {self.Balance}")
        if self.Balance != 0:
            self.AmtWtrw = int(input("Enter amount to withdraw : "))
        self.Balance = self.Balance - self.AmtWtrw
        print(f"User account name is :{self.Name} After Withdraw balance is : {self.Balance}")

    def CalculateInterest(self):
        print("-------Interest of Balance--------------")
        self.Interest = (self.Balance * BankAccount.ROI )/100
        print(f"{self.Name} Current balance is {self.Balance} its Interest is {self.Interest}")

    def Display(self):
        print(f"User account name is :{self.Name} Current balance is : {self.Balance}")

obj1 = BankAccount("Kiran", 200000)
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
obj1.Display()

