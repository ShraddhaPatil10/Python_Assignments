from sys import *
import os

def DirectoryWithExtension(path,extension):
    flag = os.path.isabs(path)

    if flag==False:
        os.path.abspath(path)

    exists = os.path.isdir(path)
    list1=[]
    if exists:
        for FolderName,SubFolder,FileName in os.walk(path):
            for filen in FileName:
                if(filen.endswith(extension)):
                    list1.append(filen)

        if(len(list1)>0):
            print("Files with extension"+extension+" are:")
            print(list1)
        else:
            print("File not found")

    else:
        print("Invalid path")

def main():
    print("Print directory names with specific extensions")

    print("Application Name is:",argv[0])
    print(len(argv))
    if(len(argv)!=3):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--H") or (argv[1]=="--h"):
        print("Help: The script is used to traverse the directory")
        exit()

    if(argv[1]=="--U") or (argv[1]=="--u"):
        print("Usage:ApplicationName extension")
        exit()

    try:
        DirectoryWithExtension(argv[1],argv[2])

    except ValueError:
        print("Invalid data type input")

    except Exception:
        print("Invalid input")


if __name__=="__main__":
    main()
