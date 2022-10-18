def Addition(values):
    sum=0
    for i in values:
        sum=sum+i

    return sum

def main():
    Arr=list()
    print("How many numbers you have to enter:")
    size=int(input())

    sum=0
    print("Enter the elements:")
    for i in range(0,size,1):
        no=int(input())
        Arr.append(no)

    print(Arr)

    Ans=Addition(Arr)
    print("Addition is:",Ans)

if __name__=="__main__":
    main()