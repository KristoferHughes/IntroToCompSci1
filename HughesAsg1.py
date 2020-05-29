#
#
# Assignment 1: this is one solution
#
#
# Kristofer Hughes
# I worked with Dominic Marchica. We collaborated on fixing any errors or roadblocks either of us ran into during the homework assignment. We helped eachother out on errors for all three problems.
#
# This file MUST BE NAMED [your last name]Asg1.ps
#
#

def nameYr():
    rax=input("Enter your first name: ")
    ray=input("Enter your last name: ")
    raz=input("Enter the four digits of your year of birth: ")
    print(rax[0:1]+"."+ray[0:1]+"."+raz[2:4])
    pass

def calcPerc():
    scr=input("Enter test score: ")
    per=input("Enter max pts available: ")
    print("Your score was: ",round(int(scr)/int(per)*100,2),"%")
    pass

def addLElements():
    frst=input("Enter position: ")
    l1=[0,1,2,3,4,5]
    l2=[100,101,102,103,104]
    print("The total at",frst,"is",l2[int(frst)]+l1[int(frst)])


    
