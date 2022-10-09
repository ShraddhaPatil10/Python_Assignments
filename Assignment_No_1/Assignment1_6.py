def chkNum(value):
    if value>0:
        print("Given number",value,"is positive")
    elif value<0:
        print("Given number",value,"is negative")
    else:
        print("Given number is zero")
    
def main():
    print("Enter one number:")
    num=int(input())

    chkNum(num)

if __name__=="__main__":
    main()
