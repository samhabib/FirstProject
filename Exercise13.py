'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

n = int(input("Give me any number and I will calculate that many Fibonnaci terms for you "))

if n == 1:

    Fib = [1]

elif n == 2:

    Fib = [1, 1]

elif n >= 3:

    Fib = [1, 1]

    for i in range(1, n-1):

        Fib.append(Fib[i - 1]+Fib[i])

print(Fib)
