#WAP to accept file name from user and check whether that file exist in current directory or not
import os

def File_Exist(FileName):
    if(os.path.exists(FileName)):
        print("Given file is exist!!!")

    else:
        print("Given file is not exist!!!")
        return

def main():
    print("Enter the file name:")
    Name=input()

    File_Exist(Name)

if __name__=="__main__":
    main()