#WAP to accept file name from user and open that file and display contents of that file
import os

def Read_File(FileName):
    if(os.path.exists(FileName)):
        fd=open(FileName,"r")
        Data=fd.read()
        print("Data from file is:")
        print(Data)

        fd.close()

    else:
        print("File is not exist!!!")
        return

def main():
    print("Enter the file name:")
    Name=input()

    Read_File(Name)

if __name__=="__main__":
    main()