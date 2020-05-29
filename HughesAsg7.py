#Kristofer Hughes
#I worked with Dominic Marchica. He helped me figure out the second function.

def unique(lst):
    "Takes a multi-dimensional list with duplicates and returns the number of unique elements in the list."
    hold=set()
    x=len(lst)
    for i in range(x):
        fone=lst[i]
        for j in range(len(fone)):
            hold.add(lst[i][j])
    end=len(hold)
    return end
    

def vote(votelst,namelst):
    "Takes a list of numbers and uses the sum to determine the winner by comparing the votes to each name from another list"
    votes=[0]*len(namelst)
    for i in votelst:
        votelst+=votes
        answ=max(votes)
        votelst.index(answ)
    print("The winner is {} with {} votes.".format(namelst,answ))
    


if __name__ == "__main__":
    def check(output, expected):
        if output != expected:
            return "FAILED!"
        else:
            return "PASSED!"
    print("RUNNING CHECK ...")
    print('unique([[0,1,1,0],[1,1,0],[0,0,1,0]]): ' + check(unique([[0,1,1,0],[1,1,0],[0,0,1,0]]),2))
    print('unique([[1,2,3,4],[5,6],[7,8,9,10,11,12]]): ' + check(unique([[1,2,3,4],[5,6],[7,8,9,10,11,12]]),12))
    print('unique([[1,2,3,1,5],[2,1,3],[5,5,2,1,3]]): ' + check(unique([[1,2,3,1,5],[2,1,3],[5,5,2,1,3]]),4))    
    print()
    print("vote([[1,0],[0,0],[0,0]],['Smith','Jones']): " + check(vote([[1,0],[0,0],[0,0]],['Smith','Jones']),'The winner is Smith with 1 votes.'))
    print("vote([[1,0],[0,100],[0,0]],['Smith','Jones']): " + check(vote([[1,0],[0,100],[0,0]],['Smith','Jones']),'The winner is Jones with 100 votes.'))          
    print("vote([[1,0,3],[0,10,1],[0,0,16]],['Smith','Jones','Williams']): " + check(vote([[1,0,3],[0,10,1],[0,0,16]],['Smith','Jones','Williams']),'The winner is Williams with 20 votes.')) 
    print()
    
