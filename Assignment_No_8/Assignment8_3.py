def Display(No):
    if(No>0):
        print(No,end="  ")
        No=No-1
        Display(No)

def main():
    print("Enter the number:")
    num=int(input())

    Display(num)

if __name__=="__main__":
    main()