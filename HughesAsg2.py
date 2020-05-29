#
#
# Assignment 2
# Kristofer Hughes
#
# I worked with Dominic Marchica. We helped eachother get started on the problems. We also help eachother work through any errors we had in our code.
# This file MUST BE NAMED [your last name]Asg2.ps
#
#
def checkID(id, validIDs):
    loc=1
    for i in range(0,len(validIDs)):
        if id.upper()==validIDs[i].upper():
            loc=i
    return(loc)
    pass


def colorNumbers(l):
    c=[]
    for i in l:
        i=i.upper()
        if i=='BLUE':
            c.append(0)
        elif i=='RED':
            c.append(1)
        elif i=='YELLOW':
            c.append(2)
        else:
            i=='  '
            c.append(3)
    c.append(-1)
    return(c)
    pass
            
def simpleSizeCheck(s,max):
    return(len(s)>max)
    pass

if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
        
    validIDs=['smith02','patel99','johnson75','philmore112','mcnaughton7']
    print('checkID("philMORE112",validIDs"): ' + check(checkID("philMORE112",validIDs),3))
    print('checkID("ferrell20",validIDs"): ' + check(checkID("farrell20",validIDs),-1))
    print('checkID("mCnaughTON7",validIDs"): ' + check(checkID("mCnaughTON7",validIDs),4))
    print('checkID("smith02",validIDs"): ' + check(checkID("smith02",validIDs),0))
    print('checkID("",validIDs"): ' + check(checkID("",validIDs),-1))
    l=["blue","red","Yellow","green","purple","BLUE","green"]
    print('colorNumbers(["blue","red","Yellow","green","purple","BLUE","green"]): ' + check(colorNumbers(l),[0, 1, 2, 3, 3, 0, 3, -1]))
    l=["green","GREEN"]
    print('colorNumbers(["green","GREEN"]): ' + check(colorNumbers(l),[ 3, 3, -1]))
    l=[]
    print('colorNumbers([]): ' + check(colorNumbers(l),[-1]))
    print('simpleSizeCheck("DPU",2): ' + check(simpleSizeCheck("DPU",2),True))
    print('simpleSizeCheck("Hello World!",7): ' + check(simpleSizeCheck("Hello World!",20),False))
    print('simpleSizeCheck("",0): ' + check(simpleSizeCheck("",0),False))
