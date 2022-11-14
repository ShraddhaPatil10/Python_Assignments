#Compare contents of two files
from sys import *
import filecmp

def Compare_Files(FileName1,FileName2):
    Res=filecmp.cmp(FileName1,FileName2)

    if(Res==True):
        print("Success")
    else:
        print("Failure")

def main():
    Compare_Files(argv[1],argv[2])

if __name__=="__main__":
    main()