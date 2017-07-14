num = input("Insert a number that you want to know all of the divisors for: ")
num = int(num)
Answer = []
x = range(1, num+1)

for element in x:
    if num % element == 0:
        Answer.append(element)

print(Answer)
