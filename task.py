import sys

def help():
    f=open("help.txt","r")
    print(f.read())
    f.close()

def ls():
    f=open("ls.txt","r")
    work=f.read()
    if work=="":
        print("No pending tasks")
    else:
        print(work)
    f.close()

def add(argv):
    priority = argv[2]
    task_name_list = argv[3:]
    task = ""
    for name in task_name_list:
        task = task + " " + name
    f=open("ls.txt","a+")
    f.seek(0)
    work=f.read()
    task1='1. '+task+' ['+str(priority)+']'
    if work=="":
        f.write(task1+'\n')
    else:
        LL=work.splitlines()
        f.close()
        f=open('ls.txt','w')
        LL.append(task1)
        #print(LL)
        prioritylist=set()
        for line in LL:
            prioritylist.add(int(line[-2]))
        prioritylist=list(prioritylist)
        prioritylist.sort()
        #print(LL)
        #print(prioritylist)
        n=1
        for num in prioritylist:
            for tasks in LL:
                if str(num)==tasks[-2]:
                    task1=str(n)+tasks[1:-2]+str(num)+']'
                    #print(task1)
                    f.write(task1+'\n')
                    LL.remove(tasks)
                    n+=1
    f.close()
    print('Added task:','"'+task+'"','with priority',priority)

def delete(argv):
    index = argv[2]
    f=open("ls.txt",'r')
    LL=f.read().splitlines()
    for line in LL:
        if line[0]==index:
            LL.remove(line)
            flag=0
            break
    else:
        print("Error: item with index",index,"does not exist. Nothing deleted.")
        flag=1
    f.close()
    if flag==0:
        f=open("ls.txt","w")
        n=1
        for line in LL:
            task1=str(n)+line[1:100]
            f.write(task1+'\n')
            n+=1
        f.close()
        print('Deleted item with index',index)

        
def done(argv):
    index = argv[2]
    f1=open("completed.txt",'a+')
    f2=open("ls.txt",'r')
    LL=f2.read().splitlines()
    for line in LL:
        if str(index)==line[0]:
            rline=line
            print("Marked item as done.")
            flag=0
            break          
    else:
        print("Error: no incomplete item with index",index,"exists.")
        flag=1
    f2.close()
    if flag==0:
        f=open("ls.txt","w")
        n=1
        for line in LL:
            if line==rline:
                pass
            else:  
                task1=str(n)+line[1:100]
                f.write(task1+'\n')
                n+=1
        f.close()
        rline=rline[0:-4]
        f1.seek(0)
        complete=f1.read()
        if complete=='':
            f1.write('1'+rline[1:100]+'\n')
        else:
            NLL=complete.splitlines()
            NLL.append(rline)
            print(NLL)
            f1.close()
            f=open("completed.txt",'w')
            n=1
            for line in NLL:
                task=str(n)+line[1:100]
                f.write(task+'\n')
                n+=1

def report():
    f1=open("completed.txt","a+")
    f1.seek(0)
    f2=open("ls.txt","a+")
    f2.seek(0)
    pend=f2.read()
    if pend=='':
        print("Pending : 0")
    else:
        PLL=pend.splitlines()
        print("Pending :",len(PLL))
        for line in PLL:
            print(line)
    done=f1.read()
    if done=='':
        print("Completed : 0")
    else:
        DLL=done.splitlines()
        print("Completed :",len(DLL))
        for line in DLL:
            print(line)


def main():
    if (len(sys.argv) <= 1):
        help()
    else:    
        option = sys.argv[1]
        if (option == "help"):
            help()
        elif (option == "ls"):
            ls()
        elif (option == "del"):
            delete(sys.argv)
        elif (option == "add"):
            add(sys.argv)
        elif (option == "done"):
            done(sys.argv)
        elif (option == "report"):
            report()

if __name__ == "__main__":
    main()
