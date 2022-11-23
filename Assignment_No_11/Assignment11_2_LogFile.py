import os
from datetime import *
import time
from sys import *
import psutil

def ProcessDisplay(log_dir="Shraddha"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    #log_path=os.path.join(log_dir,"MarvellousLog%slog"%(time.ctime()))
    log_path=os.path.join(log_dir,"MarvellosLog")
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystem Process Logger:"+time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    print("Application Name is:",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--H") or (argv[1]=="--h"):
        print("Help: This application is used to store log record of running processes")
        exit()

    if(argv[1]=="--U") or (argv[1]=="--u"):
        print("Usage: ApplicationName Absolute_Path_Of_Dir")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error:Invalid input datatype")

    except Exception:
        print("Error:Invalid Input")

if __name__=="__main__":
    main()