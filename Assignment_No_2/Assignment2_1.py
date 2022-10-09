print("Application To Demonstrate Industrial Programming")

import Arithmetic

def main():
    print("Enter 1st number:")
    num1=int(input())

    print("Enter 2nd number:")
    num2=int(input())

    Res1=Arithmetic.Add(num1,num2)
    Res2=Arithmetic.Sub(num1,num2)
    Res3=Arithmetic.Mult(num1,num2)
    Res4=Arithmetic.Div(num1,num2)

    print("Addition of",num1,"+",num2,"is=",Res1)
    print("Subtraction of",num1,"-",num2,"is=",Res2)
    print("Multiplication of",num1,"*",num2,"is=",Res3)
    print("Division of",num1,"/",num2,"is=",Res4)

if __name__=="__main__":
    main()