'''Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
 user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.'''


def splitter(test):

    answer = test.split()
    return reverse(answer)


def reverse(test):

    x = len(test)
    z = x - 1

    if x % 2 == 0:
        for D in range(z):
            if D < int(x / 2):
                temp = test[D]
                test[D] = test[z - D]
                test[z - D] = temp
    else:
        y = (x - 1) / 2
        y = int(y)

        for E in range(z):
            if E < y:
                temp = test[E]
                test[E] = test[z - E]
                test[z - E] = temp

    return test

testString = input("Type in a long string of words and I shall return them in reverse order: ")

result = " ".join(splitter(testString))

print(result)
