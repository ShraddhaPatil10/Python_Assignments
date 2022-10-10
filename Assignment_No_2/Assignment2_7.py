def main():
    print("Enter the number:")
    num=int(input())

    for i in range(1,num+1,1):
        for j in range(1,num+1,1):
            print(j,end="  ")

        print("\n")

if __name__=="__main__":
    main()