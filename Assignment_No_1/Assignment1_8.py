def Pattern():
    print("Enter the number:")
    num=int(input())

    i=0

    while i<num:
        print("*",end="   ")
        i=i+1

if __name__=="__main__":
    Pattern()