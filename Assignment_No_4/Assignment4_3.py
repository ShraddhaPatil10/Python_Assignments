def Greater(values):
    return (values>=70 and values<=90)

def Increase(values):
    return values+10

def Product(A,B):
    return A*B

def filterX(Helper_function,data):
    Result=[]
    for no in data:
        if(Helper_function(no)==True):
            Result.append(no)

    return Result

def mapX(Helper_function,data):
    Result=[]
    for no in data:
        values=Helper_function(no)
        Result.append(values)

    return Result

def reduceX(Helper_function,data):
    Ans=1
    for no in data:
        Ans=Helper_function(Ans,no)

    return Ans

def main():
    Arr=list()
    print("How many numbers do you want to enter:")
    size=int(input())

    print("Enter the numbers:")
    for i in range(0,size,1):
        no=int(input())
        Arr.append(no)

    print("Data is:",Arr)

    data_filter=filterX(Greater,Arr)
    print("Data after filter:",data_filter)

    data_map=mapX(Increase,data_filter)
    print("Data after map:",data_map)

    Result=reduceX(Product,data_map)
    print("Data after reduce:",Result)

if __name__=="__main__":
    main()
