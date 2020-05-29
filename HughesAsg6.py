#
# Kristofer Hughes
# Dominic Marchica and Matt Davis: I worked with Dominic and Matt on this homework assignment. We basically had a brainstorming session on how to get started on the problems and helped eachother fix errors in our code.
#
#

import os   # this is required to do the empty file check 

def showNames(ifile):
    badlst=[]
    try:
        infile=open(ifile)
        content=infile.readlines()
        infile.close()
        for i in content:
            hold=i.split()
            badlst.append(hold[0])
    except FileNotFoundError:
        badlst.append(-1)
    badlst.sort()
    return badlst

    
def calcAvg(ifile):
    scores=[]
    total=0
    s1=""
    students=len(scores)
    average=int(total/students)
    try:
        infile=open(ifile)
        content=infile.readlines()
        infile.close()
        for i in content:
            newContent=i.split()
            try:
                scores.append(int(newContent[2]))
            except ValueError:
                print("Non-numeric found.")
        for i in scores:
            total=total+i
            students=len(scores)
            average=int(total/students)
    except FileNotFoundError:
        print("File not found.")
    return ("{} Total number of students: {}  Average score: {}".format(s1,students,average))


def studentAvg(ifile):
    outpt=[]
    grad=[]
    t1=""
    try:
        infile=open(ifile)
        content=infile.readlines()
        infile.close()
        for i in content:
            total=0
            newContent=i.split()
            sublist=newContent[2:]
            for i in sublist:
                try:
                    total=total+int(i)
                except ValueError:
                    s1="Error! Non-numeric!"
            print(sublist)
        if os.stat(ifile).st_size == 0:
                output="File is empty."
    except FileNotFoundError:
        output="File not found."
    return(outpt)
    

# this is the code for checking if a file is empty.
# Put this after your open
# Add try/except appropriately
# its been commented out to run the auto checks for the other functions

##        if os.stat(ifile).st_size == 0: # note: it uses the stat method from os
##            raise ValueError
    

if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
    print("RUNNING CHECK ...")
    #print('showNames(ifile): ' + check(showNames("nosuchfile.txt"),[-1]))
    print('showNames(ifile): ' + check(showNames("grades1.txt"),['Domel', 'Fischer', 'Hope', 'Patel']))
    print('showNames(ifile): ' + check(showNames("grades2.txt"),['Domel', 'Fischer']))
    print()
    print('calcAvg(ifile): ' + check(calcAvg("nosuchfile.txt"),'File not found.'))
    print('calcAvg(ifile): ' + check(calcAvg("grades1.txt"),'Non-numeric found. Total number of students: 3  Average score: 96'))
    print('calcAvg(ifile): ' + check(calcAvg("grades2.txt"),'Non-numeric found. Total number of students: 1  Average score: 90'))
    print()
    print('studentAvg(ifile): ' + check(studentAvg("nosuchfile.txt"),'File not found.'))
    print('studentAvg(ifile): ' + check(studentAvg("grades1.txt"),['Error! Non-numeric! Name: Domel Number of assignments: 7 Average score: 81.42857142857143', 'Name: Fischer Number of assignments: 8 Average score: 74.125', 'Name: Hope Number of assignments: 8 Average score: 100.0', 'Name: Patel Number of assignments: 8 Average score: 90.375']))
    print('studentAvg(ifile): ' + check(studentAvg("grades2.txt"),['Error! Non-numeric! Name: Domel Number of assignments: 7 Average score: 0.0', 'Name: Fischer Number of assignments: 8 Average score: 90.0']))
    print('studentAvg(ifile): ' + check(studentAvg("grades3.txt"),'File is empty.'))


            
