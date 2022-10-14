def main():
    print("Enter the number:")
    num=int(input())

    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1

    if cnt<=2:
        print("Given number",num,"is prime number")
    else:
        print("Given number",num,"is not prime")
        
if __name__=="__main__":
    main()