power = lambda no : 2**no

def main():
    print("Enter one number:")
    num=int(input())

    Ans=power(num)
    print("Power of",num,"is=",Ans)

if __name__=="__main__":
    main()