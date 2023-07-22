import multiprocessing
import os

def fun(number):
    print("Parent process ID of fun:",os.getppid())
    print("Process ID of fun:",os.getpid())

    for i in range(number):
        print(i)

def gun(number):
    print("Parent process ID of gun:",os.getppid())
    print("Process ID of gun:", os.getpid())
    for i in range(number):
        print(i)

def main():
    print("Total cores available:",multiprocessing.cpu_count())

    print("Parent process ID of main:", os.getppid())
    print("Process ID of main:", os.getpid())

    number=3
    result=None

    p1=multiprocessing.Process(target=fun,args=(number,))
    p2=multiprocessing.Process(target=gun,args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__=="__main__":
    main()