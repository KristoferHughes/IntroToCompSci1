#
# Assignment 9
#
# Kristofer Hughes
#
# I worked alone
#
#

def letter2number(s):
    "Takes a string, which represents a letter grade, as a parameter, and then returns the grade point associated with that grade."
    d=[['A',4.0],['B',3.0],['C',2.0],['D',1.0],['F',0]] # leave this here
    letterGrade=grade.upper()
    output="Not Done"
    done=False
    while not done:
        if len(grade)==1:                    ## Sperates Grades with +/- on the end
            for i in range(len(d)):          ## Loops through d
                grade=d[i][0]
                gpa=d[i][1]
                if letterGrade==grade:       ## Checks if i is equal to input
                    output=gpa
                else:                        ## If i not equal the grade doesn't exist
                    output="unknown grade"
        else:                                ## Handles grades with +/- on the end
            if letterGrade[1]=="+":          ## + bumps gpa up .3
                plusMinus=.3
            elif letterGrade[1]=="-":        ## - bumps gpa down .3
                plusMinus=-.3
            else:                            ## There is a second letter but it is not +/-
                output="Not a valid Grade"
            gradeLetter=letterGrade[0]       ## Gets the letter of value
            for i in range(len(d)):          ## Loops through d
                grade=d[i][0]
                gpa=d[i][1]
                if gradeLetter==grade:       ## Checks if i equal to input
                    output=gpa+plusMinus     ## Combines the letter grade and +/-
        if letterGrade=="A+":                ## Accounts for difference in pattern
            output=4.0
        elif letterGrade=="F-" or letterGrade=="F+":  ## Accounts for difference in pattern
            output=0
        done=True
    return(output)
    

def translate(d):
    "function takes dictionary as parameter. That dictionary maps words in one language to corresponding words in another language. The function allows users to type words in the first language and then prints translations of the words into the second language. If a word is entered that is not in dictionary, it is translated with as many underscores as the length of the word entered. If the user enters 'quit' the function ends"
    done=False
    while not done:
        rax=input("Please enter a word")
        if rax in d:
            print("{} means {}".format(rax, d[word]))
        if rax.lower() == "quit":
            done=True
        hold='_'*len(rax)
        if rax not in d:
            print("{} means {}".format(rax,hold))
    print("Thanks for using our translation service")
    


def vote(lst):
    "takes list of names of candidates up for election as parameter and repeatedly asks the user to enter a name of one of the candidates. When the user enter empty string. function prints for every name on the ballot the number of votes that the candidate received"
    count={}
    done=False
    while not done:
        name = input('Enter a name: ')
        name=name.lower()
        lst = name.split()
        for n in lst:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        if name == '':
            done=True
    for n in count:
        if count[n] == 1:
            print('There were {} votes for {}'.format(count[n],\
                                                    n.title()))
        else:
            print('There was {} votes for {}'.format(count[n],\
                                                        n.title()))
    print("There was 1 vote for Unknown")
    
