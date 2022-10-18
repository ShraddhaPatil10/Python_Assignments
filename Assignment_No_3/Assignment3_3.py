def min(no):
    min=0
    for data in no:
        if (data < min):
            min = no

    return min

def main():
    Arr=list()
    print("How many elements you want to enter:")
    size=int(input())

    print("Enter the elements:")
    for i in range(0,size,1):
        no=int(input())
        Arr.append(no)

    Ans=min(Arr)
    print("Minimum element is:",Ans)

if __name__=="__main__":
    main()