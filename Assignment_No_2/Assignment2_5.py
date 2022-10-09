def main():
    print("Enter the number:")
    num=int(input())

    if num>0:
        if num%2==0:
            print("Given number",num,"is not prime number")
        else:
            print("Given number",num,"is prime")
    else:
        print("Given number",num,"is not prime")
        
if __name__=="__main__":
    main()