def fun(val,ele):
    cnt=0
    for i in val:
        if(i==ele):
            cnt+=1
    return cnt

def main():
    Arr=list()

    print("How many numbers you have to enter:")
    size=int(input())

    print("Enter the numbers:")
    for i in range(0,size,1):
        no=int(input())
        Arr.append(no)

    print("Enter the element to search:")
    ele=int(input())

    Ans=fun(Arr,ele)

    print("Frequency of",ele,"in given list is:",Ans)
 
if __name__=="__main__":
    main()

