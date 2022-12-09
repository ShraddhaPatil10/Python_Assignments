import os
import time
from sys import *
import psutil

def ProcessDisplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%slog"%(time.time()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    print("Marvellous Processor logger:" + time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


    for ele in listprocess:
        f.write("%s\n"%ele)

def main():
    print("--------------------------Shraddha Patil--------------------------")
    print("Application Name is:",argv[0])

    if len(argv)!=2:
        print("Invalid number of arguments")
        exit()

    if (argv[1]=="--h") or (argv[1]=="--H"):
        print("Help:This script used to display log record of running processes")
        exit()

    if (argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage:ApplicationName Absolute_path_of_dir")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Invalid input datatype")

    except Exception:
        print("Invalid input")

if __name__=="__main__":
    main()

