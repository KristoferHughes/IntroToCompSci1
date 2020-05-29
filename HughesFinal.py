#
# Kristofer Hughes
# Final exam CSC241
# 

# Problem 1

def buildDict(k1,k2,v2):
    d={}
    for i in range(len(k1)):
        citylst=(k1[i],k2[i])
        stlst=v2[i]
        d.update({citylst:stlst})
    return d
    

# Problem 4

def jump(lst,stpt):
    done=False
    output=[]
    chekdNum=[]
    while not done:
        try:
            if stpt>0:
                if stpt not in chekdNum:
                    chekdNum.append(stpt)
                    output.append(lst[stpt][0])
                    stpt=lst[stpt][1]
                else:
                    done=True
            else:
                raise IndexError
        except IndexError:
            done=True
    if len(output)==0:
        output=[]
    else:
        output.append(len(output))
    return(output)
    

# Problem 6

def milestostrides(ifile):
    output=[]
    stridesInMile=63360/53
    infile=open(ifile)
    content=infile.read()
    infile.close()
    content=content.split("\n")
    for i in content:
        try:
            newContent=i.split(";")
            start=newContent[0]
            end=newContent[1]
            milage=float(newContent[2])
            totalStrides=round(milage*stridesInMile*2)
            totalStrides=str("{:,}".format(totalStrides))+" strides"
            if start=="" or end=="" or milage=="" or milage<1:
                raise ValueError
            line=[start,end,totalStrides]
        except ValueError:
            line="ERROR: Invalid input found in this line: {};{};{}".format(start,end,newContent[2])
        output.append(line)
    return(output)
        
# Problem 7

def addstring(s,n):
    newStrng=""
    total=0
    string=""
    for i in range(n,len(s)):
        newStrng=newStrng+s[i]
    newStrng=newStrng.split("*")
    for i in newStrng[0]:
        try:
            total=total+int(i)
        except ValueError:
            string=string+i
    if total==0:
        output=-1
    else:
        output=total
    return(output)

            
    


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
    print("RUNNING CHECK ...")
    print()
    print("PROBLEM 1")
    print("buildDict(['Chicago','Detroit','New York','Seattle'],['IL','MI','NY','WA'],['a102','a44','b33','c3']): "+ check(buildDict(['Chicago','Detroit','New York','Seattle'],['IL','MI','NY','WA'],['a102','a44','b33','c3']),{('New York', 'NY'): 'b33', ('Detroit', 'MI'): 'a44', ('Seattle', 'WA'): 'c3', ('Chicago', 'IL'): 'a102'}))
    d=(buildDict(['Chicago','Detroit','New York','Seattle'],['IL','MI','NY','WA'],['a102','a44','b33','c3']))
    print("d[('Seattle','WA')]: "+check(d[('Seattle','WA')],'c3'))
    print("d[('Chicago','IL')]: "+check(d[('Chicago','IL')],'a102'))
    print()
    print("PROBLEM 4")
    lst=[['a',8],['b',2],['c',7],['d',1],['e',5],['f',0],['g',5],['h',8],['i',1]]
    print("jump(lst,2): "+check(jump(lst,2),['c','h','i','b',4]))
    print("jump(lst,11): "+check(jump(lst,11),[]))
    print("jump(lst,-1): "+check(jump(lst,-1),[]))
    print("jump(lst,8): "+check(jump(lst,8),['i','b','c','h',4]))
    print("jump(lst,3): "+check(jump(lst,3),['d','b','c','h','i',5]))
    print()
    print("PROBLEM 6")
    print("milestostrides('mileage1.txt'): "+check(milestostrides('mileage1.txt'),['ERROR: Invalid input found in this line: Chicago;Austin;0',['Chicago', 'Washington D.C', '1,420,675 strides'], ['Chicago', 'Milwaukee', '194,910 strides'], 'ERROR: Invalid input found in this line: Chicago;;99', 'ERROR: Invalid input found in this line: Chicago;Detroit;ttt', 'ERROR: Invalid input found in this line: Chicago;;', 'ERROR: Invalid input found in this line: ;;', 'ERROR: Invalid input found in this line: Chicago;Richmond;-9', ['Chicago', 'San Diego', '4,144,700 strides']]))
    print("milestostrides('mileage.txt'): "+check(milestostrides('mileage.txt'),[['Chicago', 'Washington D.C', '1,420,675 strides'], ['Chicago', 'Milwaukee', '194,910 strides'], ['Chicago', 'San Diego', '4,144,700 strides']]))
    print()
    print("PROBLEM 7")
    print("addstring('abcdefg',3): "+check(addstring('abcdefg',3),-1))
    print("addstring('1abcd1efg',3): "+check(addstring('1abcd1efg',3),1))
    print("addstring('1abcd*1efg',0): "+check(addstring('1abcd*1efg',0),1))
    print("addstring('1abcd1efg*',0): "+check(addstring('1abcd1efg*',0),2))
    print("addstring('',0): "+check(addstring('',0),-1))
    print("addstring('',55): "+check(addstring('',55),-1))
    print("addstring('12345*6789',0): "+check(addstring('12345*6789',0),15))
    print("addstring('12345*6789',6): "+check(addstring('12345*6789',6),30))
