''' Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
 (If you don’t know what a divisor is, it is a number that divides evenly into another number.) '''


num = input("Insert a number that you want to know all of the divisors for: ")
num = int(num)
Answer = []
x = range(1, num+1)

for element in x:
    if num % element == 0:
        Answer.append(element)

print(Answer)
