def factorial(num):
    fact=1
    i=1
    while i<=num:
        fact=fact*i
        i=i+1

    return fact

def main():
    print("Enter the number:")
    no=int(input())

    Ans=factorial(no)

    print("Factorial of",no,"is=",Ans)

if __name__=="__main__":
    main()