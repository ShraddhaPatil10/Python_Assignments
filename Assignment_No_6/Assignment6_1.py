class BookStore:
    No_of_books=0
    def __init__(self):
        print("Inside init method")
        self.Name=""
        self.Author=""

        print("Enter the name of the book:")
        self.Name=input()

        print("Enter the author name:")
        self.Author=input()

        BookStore.No_of_books=BookStore.No_of_books+1


    def Display(self):
        print("Name of book:",self.Name)
        print("Author of book:",self.Author)
        print("Number of books:",BookStore.No_of_books)

def main():
    obj1=BookStore()
    print("-------------------------------------------------------")
    obj1.Display()

    print("**********************************************")
    obj2=BookStore()
    print("----------------------------------------------------")
    obj2.Display()

if __name__=="__main__":
    main()