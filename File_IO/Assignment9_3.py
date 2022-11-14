#Copy content of existing file to newly created file
def copy_file(FileName):
    fd1=open(FileName,"w")
    fd2=open("Demo.txt")

    for line in fd2:
        fd1.write(line)

    fd1.close()
    fd2.close()

def main():
    print("Enter the file name:")
    Name1=input()

    copy_file(Name1)

if __name__=="__main__":
    main()