def Factorial(No):
    if(No<=0):
        return 1

    else:
        return (No * Factorial(No-1))


def main():
    print("Enter the number:")
    num=int(input())

    output=Factorial(num)

    print("Factorial is:",output)

if __name__=="__main__":
    main()