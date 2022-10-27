class Circle:
    PI=3.14
    def __init__(self):
        self.Area=0.0
        self.Radius=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter the radius:")
        self.Radius=float(input())

    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def display(self):
        print("Radius of circle:",self.Radius)
        print("Area of circle:",self.Area)
        print("Circumference of circle:",self.Circumference)

def main():
    obj=Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.display()

if __name__=="__main__":
    main()