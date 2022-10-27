class Demo:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Fun(self):
        print("Inside Fun")
        print(self.no1)
        print(self.no2)
        print("****************************************")

    def gun(self):
        print("Inside gun")
        print(self.no1)
        print(self.no2)
        print("******************************************")

def main():
    print("Enter 1st number:")
    num1=int(input())

    print("Enter 2nd number:")
    num2=int(input())

    print("Enter 3rd number:")
    num3=int(input())

    print("Enter 4th number:")
    num4=int(input())

    obj1=Demo(num1,num2)
    obj2=Demo(num3,num4)

    obj1.Fun()
    obj2.Fun()

    obj1.gun()
    obj2.gun()

if __name__=="__main__":
    main()