def main():
    Arr=list()
    print("How many elements you want to enter:")
    size=int(input())

    max=0
    print("Enter the elements:")
    for i in range(0,size,1):
        no=int(input())
        #Arr.append(no)

        if(no>max):
            max=no

    print("Maximum element is:",max)

if __name__=="__main__":
    main()