def main():
    print("Enter the number:")
    num=int(input())

    for i in range(num,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")

        print("\n")

if __name__=="__main__":
    main()