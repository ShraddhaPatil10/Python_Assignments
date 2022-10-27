class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0


    def Accept(self):
        print("Enter 1st value:")
        self.value1=int(input())

        print("Enter 2nd value:")
        self.value2=int(input())


    def Addition(self):
        return self.value1+self.value2

    def Substraction(self):
        return self.value1-self.value2

    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2

def main():
    obj=Arithmetic()

    obj.Accept()

    Ans=obj.Addition()
    print("Addition is:",Ans)

    Ans=obj.Substraction()
    print("Substraction is:",Ans)

    Ans=obj.Multiplication()
    print("Multiplication is:",Ans)

    Ans=obj.Division()
    print("Division is:",Ans)

if __name__=="__main__":
    main()