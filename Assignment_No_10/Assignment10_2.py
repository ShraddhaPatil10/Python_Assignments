import os
from sys import *

def DirectoryReplaceExtension(path,ext1,ext2):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for folderName,subfolder,fileName in os.walk(path):
            for filen in fileName:
                if(filen.endswith(ext1)):
                    new = os.path.splitext(path)[0]
                    os.rename(filen,new + ext2)

    else:
        print("File not found")

def main():
    print("Script to replace file extensions")

    print("Application Name is:",argv[0])

    if(len(argv)!=4):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage: ApplicationName Absolute_path_of_directory exetension1 extension2")
        exit()

    if(argv[1]=="--h") or (argv[1]=="--H"):
        print("Help:Script is used to replace extensions")
        exit()

    try:
        DirectoryReplaceExtension(argv[1],argv[2],argv[3])

    except ValueError:
        print("Invalid input datatype")

    except Exception:
        print("Invalid input")

if __name__=="__main__":
    main()