Multiply = lambda no1,no2 : no1*no2

def main():
    print("Enter 1st number:")
    num1=int(input())

    print("Enter 2nd number:")
    num2=int(input())

    Ans=Multiply(num1,num2)
    print("Multiplication of",num1,"and",num2,"is=",Ans)

if __name__=="__main__":
    main()
