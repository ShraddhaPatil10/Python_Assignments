def main():
    print("Enter one number:")
    num=int(input())

    for i in range(1,num+1):
        for j in range(1,num+1):
            print("*",end=" ")
        print("\n")

if __name__=="__main__":
    main()