from sys import *

def Factor(no):
    print("Factors are:")
    i=1
    sum=0

    while(i<=int(no/2)):
        if(no%i==0):
            print(i)
            sum=sum+i
        i=i+1;
    return sum

def main():
    num=0
    Res=Factor(int(argv[1]))

    print("Addition of factors is:",Res)

if __name__=="__main__":
    main()