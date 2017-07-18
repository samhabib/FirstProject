'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
 first and last elements of the given list. For practice, write this code inside a function.'''

a = [5, 10, 15, 20, 25]

def firstAndLast(numList):
    if numList == []:
        print("The list has no values")
    else:
        print("The first number in the list is %s and the last number in the list is %s" % (numList[0], numList[len(numList)-1]))
        return [numList[0], numList[len(numList)-1]]

firstAndLast(a)