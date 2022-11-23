import os.path
from sys import *
import hashlib

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if(flag==False):
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}
    if exists:
        for FolderName,SubFolder,FileName in os.walk(path):
            for filen in FileName:
                path=os.path.join(FolderName,filen)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups

    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicate found")
        print("The following files are identical")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print("\t\t%s"%subresult)

    else:
        print("No duplicate files are found")

def DeleteDuplicate(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    icnt=0
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0

    else:
        print("No duplicate found")

def main():
    print("Application Name is:",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--h") or (argv[1]=="--H"):
        print("Help:This application is used to delete duplicate files")
        exit()

    if(argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage:ApplicationName Absolute_path_of_dir")
        exit()

    try:
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)
        DeleteDuplicate(arr)

    except ValueError:
        print("Invalid datatype input")

    except Exception:
        print("Invalid input")

if __name__=="__main__":
    main()
