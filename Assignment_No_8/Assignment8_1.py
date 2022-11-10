def Display(No):
    if(No>0):
        print("*",end="  ")
        No=No-1
        Display(No)

def main():
    print("Enter any number:")
    num=int(input())

    Display(num)

if __name__=="__main__":
    main()