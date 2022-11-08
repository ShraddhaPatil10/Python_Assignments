class BankAccount:
    ROI=10.5
    def __init__(self):
        self.Name=""
        self.Amount=0

        print("Enter Name of customer:")
        self.Name=input()

        print("Enter amount:")
        self.Amount=int(input())

    def Display(self):
        print("Name of customer:",self.Name)
        print("Your current Amount is:",self.Amount)

    def Deposite(self):
        print("How much amount you want to deposite:")
        self.Dep=int(input())

        self.Amount=self.Amount-self.Dep

    def Withdraw(self):
        print("How much amount you want to withdraw:")
        self.Withdraw_amount=int(input())

        self.Amount=self.Amount-self.Withdraw_amount

    def CalculateIntrest(self):
        self.Intrest=(BankAccount.ROI*self.Amount)/100
        print("Intrest amount is:",self.Intrest)

def main():
    print("*******************1st customer***************")
    obj1=BankAccount()
    obj1.CalculateIntrest()
    obj1.Deposite()
    obj1.Withdraw()
    obj1.Display()

    print("********************2nd customer*********************")
    obj2=BankAccount()
    obj2.CalculateIntrest()
    obj2.Deposite()
    obj2.Withdraw()
    obj2.Display()

if __name__=="__main__":
    main()

