 
f=open("macrocode.txt","r")
f1=open("mnt.txt","w")
f2=open("fppt.txt","w")
f4=open("mdt.txt","w")
mname=list()
fp=list()
pp=list()
lines=f.readlines()
x=1
y=0
for i in xrange(len(lines)):
    line=lines[i]
    words=line.split()
    if "MACRO" in words:
        ch=line.count('&')
        f1.write(words[1]+" "+str(ch)+" "+str(i)+"\n")
        while ch!=0:
            f2.write(words[1]+" "+words[-ch]+" "+str(x)+"\n")
            name=words[1]
            mname.append(words[1])
            fp.append(words[-ch])
            pp.append(str(x))
            ch=ch-1
            x=x+1 
        f2.write("\n")
        i=i+1
        line=lines[i]
        words=line.split()
        while "MEND" not in words:
                if words[-1] in fp:
                       y=fp.index(words[-1]) 
                       f4.write(mname[y]+" "+words[0]+" "+pp[y]+"\n")
                       
                else:
                       f4.write(name+" "+words[0]+" "+words[-1]+"\n")
                i=i+1 
                line=lines[i]
                words=line.split()
                y=0
        f4.write(words[0]+"\n")
        x=1    
f1.close()
f2.close()
f.close()
f4.close()  
f=open("macrocode.txt","r")
f1=open("mnt.txt","r")
f5=open("papt.txt","w")
lines=f.readlines()
lines1=f1.readlines()
for i in xrange (len(lines)):
    line=lines[i]
    words=line.split()
    for j in xrange(len(lines1)):
        line1=lines1[j]
        words1=line1.split()
        if words[0]==words1[0]:
            x=int(words1[-2])
            y=1 
            while x!=0:
                f5.write(words[0]+" "+str(y)+" "+words[-x]+"\n")
                y=y+1 
                x=x-1
f.close()
f1.close()
f5.close()
operation={'STORE','LOAD','MULT','ADD','SUB','DIV','END'}
f=open("macrocode.txt","r")
f1=open("mnt.txt","r")
f2=open("fppt.txt","r")
f4=open("mdt.txt","r")    
f5=open("papt.txt","r")
f3=open("expandedcode.txt","w")
lines1=f4.readlines()
lines2=f5.readlines()
for line in f:
    words=line.split()
    if "MACRO" in words:
          for line in f:
              words=line.split()
              if "MEND" not in words:
                  continue
              else:
                  break
    else:
        if words[0] in operation:
          f3.write(line)
        else:
         for j in xrange(len(lines1)):
            line1=lines1[j]
            words1=line1.split()
            if words1[0]==words[0]:
                for k in xrange(len(lines2)):
                    line2=lines2[k]
                    words2=line2.split()
                    if words[0]==words2[0] and words1[-1]==words2[-2]:
                        f3.write(words1[1]+" "+words2[-1]+"\n")
                        flag=0
                        break
                    else:
                        flag=1
                if flag==1:
                    line1=lines1[j]
                    words1=line1.split()
                    print (words1[0],words1[1],words1[2])
                    f3.write(words1[1]+" "+words1[-1]+"\n")
                    flag=0
                
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
            

