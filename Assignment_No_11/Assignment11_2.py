from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isdir(path)

    if flag==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups={}
    if(exists):
        for FolderName,SubFolder,FileName in os.walk(path):
            for filen in FileName:
                path = os.path.join(FolderName,filen)
                filehash = hashfile(path)


                if filehash in dups:
                    dups[filehash].append(path)
                else:
                    dups[filehash]=[path]

        return dups

    else:
        print("Invalid Path")

def PrintDuplicates(Dict1):
    results=list(filter(lambda x:len(x)>1,Dict1.values()))

    if(len(results)>0):
        print("Duplicate Found")
        print("Following are identical files:")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if(icnt>=2):
                    print("\t\t%s"%subresult)

    else:
        print("No duplicate files found")

def main():
    print("Application Name is:",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--h") or (argv[1]=="--H"):
        print("Help: Display names of duplicate files")
        exit()

    if(argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage: ApplicationName Absolute_Path_of_Dir")
        exit()

    try:
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDuplicates(arr)

    except ValueError:
        print("Invalid input datatype")

    except Exception:
        print("Invalid input")

if __name__=="__main__":
    main()