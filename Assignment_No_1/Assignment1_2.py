def chkNum():
    print("Enter one number:")
    num=int(input())

    if num%2==0:
        print("The given number",num,"is even")

    else:
        print("The given number",num,"is odd")

if __name__=="__main__":
    chkNum()