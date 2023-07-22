import os
import time
import psutil
import smtplib
import schedule
from sys import *
import urllib.request
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('https://www.wikipedia.org/', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def MailSender(fileneme, time):
    try:
        fromaddr = "shraddhapatil14310@gmail.com"
        toaddr = "vp1576410@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Please find the attached document which contains log of running process.
        Log file is created at:%s

        This is auto generated mail.

        Thanks and Regards,
        Shraddha Patil
        """ % (toaddr, time)

        subject = """
        Process log generated at:%s
        """ % (time)

        msg['subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(fileneme, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', 'attachment:filename=%s' % fileneme)

        msg.attach(p)

        s = smtplib.SMTP("smtp.gmail.com", 587)

        s.starttls()

        s.login(fromaddr,"oyiqdbrwfloeffzc")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent through mail")

    except Exception as E:
        print("Unable to sent through mail", E)

def ProcessLog(log_dir="LogFile"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "LogFile%s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Process Logger:%s" % time.time() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            arr = FindDuplicate(argv[1])
            PrintDuplicate(arr, argv[1])
            DeleteDuplicate(arr)
            listprocess.append(arr)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location", (log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, time.time())
        endTime = time.time()

        print("Took %s seconds to send mail" % (endTime - startTime))

    else:
        print("There is no internet connection")
def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)

    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)

    if flag == False:
        path=os.path.abspath(path)

    exists = os.path.isdir(path)
    dups={}

    if exists:
        for DirName,Subfolder,FileName in os.walk(path):
           # print("Current Folder is" +DirName)

            for filen in FileName:
                path = os.path.join(DirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)

                else:
                    dups[file_hash]=[path]

        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(Dict1,log_dir="Shraddha"):
    listprocess=[]
    results = list(filter(lambda x: len(x)>1,Dict1.values()))

    if os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%time.time())
    f=open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystem process logger:"+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("Duplicate files are:")

    if len(results)>0:
        print("Duplicate Found")
        print("The following files are identical:")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    #print("\t\t%s"%subresult)
                    listprocess.append(subresult)

    else:
        print("No duplicate files found")

    for element in listprocess:
        f.write("%s\n"%element)

def DeleteDuplicate(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))

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
    print("\n\n********************PROCESS LOG WITH PERIODIC MAIL SENDING FACILITY********************\n\n")
    print("Application Name:" + argv[0])

    if (len(argv) != 2):
        print("Error:Invalid number of arguments")
        exit()

    if (argv[1] == "--H") or (argv[1] == "--h"):
        print("This script is used log record of running processes")
        exit()

    if (argv[1] == "--U") or (argv[1] == "--u"):
        print("Usage:ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error:Invalid Datatype Input")

    except Exception as E:
        print("Error:Invalid Input", E)

if __name__ == "__main__":
    main()