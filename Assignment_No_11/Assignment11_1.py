import os
from sys import *
import hashlib

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)

    if(flag==False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if(exists):
        for FolderName,Subfolder,FileName in os.walk(path):
            for filen in FileName:
                path = os.path.join(FolderName,filen)
                file_hash = hashfile(path)

            print(path)
            print("Checksum is:",file_hash)
            print(" ")

    else:
        print("Invalid Path")
        
def main():
    print("Application Name is:",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--H") or (argv[1]=="--h"):
        print("Help: This application is used to find checksum")
        exit()

    if(argv[1]=="--U") or (argv[1]=="--u"):
        print("Usage: ApplicationName Absolute_Path_Of_Dir")
        exit()

    try:
        DisplayChecksum(argv[1])

    except ValueError:
        print("Invalid input datatype")

    except Exception:
        print("Invalid Input")

if __name__=="__main__":
    main()