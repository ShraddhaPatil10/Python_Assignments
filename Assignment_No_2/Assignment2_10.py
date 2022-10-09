def main():
    print("Enter the number:")
    num=int(input())

    cnt=0
    dig=0
    sum=0
    while num>0:
        dig=num%10
        sum=int(sum)+int(dig)
        num=num/10

    print("The sum of digits is:",sum)

if __name__=="__main__":
    main()