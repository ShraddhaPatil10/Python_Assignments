class Numbers:
    def __init__(self):
        self.value=0
        print("Enter the value:")
        self.value=int(input())

    def Factors(self):
        for i in range(1,self.value,1):
            if(self.value%i==0):
                print(i)

    def SumFactor(self):
        sum=0
        for i in range(1,self.value,1):
            if(self.value%i==0):
                sum=sum+i

        return sum

    def CheckPrime(self):
        Res=self.SumFactor()

        if(Res==1):
            return True
        else:
            return False

    def CheckPerfect(self):
        Res=self.SumFactor()

        if(self.value==Res):
            return True
        else:
            return False

def main():
    obj1=Numbers()
    print("Factors are:")
    obj1.Factors()

    Ans=obj1.SumFactor()
    print("Sum of factors is:",Ans)

    Ans=obj1.CheckPrime()
    if(Ans==True):
        print("Given number is prime")
    else:
        print("Given number is not prime")

    Ans=obj1.CheckPerfect()
    if(Ans==True):
        print("Given number is perfect number")
    else:
        print("Given number is not perfect number")


if __name__=="__main__":
    main()