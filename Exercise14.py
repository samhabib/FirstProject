'''Write a program (function!) that takes a list and returns a new list that contains all the elements of
the first list minus all the duplicates.

Extras:
    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def noDupeList( varList ):

    answer = []
    for x in varList:
        if x not in answer:
            answer.append(x)

    print(answer)

def noDupeSet( varList ):
    varList = set( varList)
    print(varList)


a = [3, 1, 1, 7, 19, 'Sam', 'Kenny', 'Kenny']

noDupeList(a)
noDupeSet(a)
print(len(a))