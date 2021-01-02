import os
t=open('password.txt')
line=t.readline()
flag=0
print("Please input the file name")
pic=input()
while line:
    line=line[0:-1]
    #st="steghide extract -sf '%s' -p '%s' > break.txt"%(pic,line)
    result=os.popen("steghide extract -sf '%s' -p '%s' "%(pic,line)).read()
    result=os.popen("steghide extract -sf '%s' -p '%s' "%(pic,line)).read()
    print(line)
    #result = open('break.txt', 'r')
    print("HELLO"+result)
    if "wrote" in result:
        print("password:" + line)
        print(result)
        flag=1
        break
    line=t.readline()
if flag==0:
    print("Unable to find the password")