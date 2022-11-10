def Display(No,i):
    if(i<=No):
        print(i,end="  ")
        i=i+1
        Display(No,i)

def main():
    print("Enter the number:")
    num=int(input())

    i=1
    Display(num,i)

if __name__=="__main__":
    main()