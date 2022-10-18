def Even(no):
    return no%2==0

def Square(no):
    return no*no

def Add(A,B):
    return A+B

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

def reduceX(Helper_fumction,data):
    Ans=0
    for no in data:
        Ans=Helper_fumction(Ans,no)

    return Ans

def main():
    Arr=list()
    print("How many numbers do you want to enter:")
    size=int(input())

    print("Enter the elements:")
    for i in range(0,size,1):
        no=int(input())
        Arr.append(no)

    print("Data is:",Arr)

    data_filter=filterX(Even,Arr)
    print("Data after filter:",data_filter)

    data_map=mapX(Square,data_filter)
    print("Data after map:",data_map)

    Result=reduceX(Add,data_map)
    print("Data after map:",Result)

if __name__=="__main__":
    main()