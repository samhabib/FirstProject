'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a
prime number is a number that has no divisors.)'''

primeNumber = input("Give me a number and I will tell you if it is prime! ")

primeNumber = int(primeNumber)
if primeNumber % 2 == 0:
    print("No %s is not a prime number" % primeNumber)

else:
    n = 3
    Test = (primeNumber + 1)/2
    Test = int(Test)

    while n <= Test:

        if primeNumber % n == 0:

            print("No %s is not a prime number" % primeNumber)
            n = 0
            break

        else:

            n += 1

    if n != 0:
        print("Yes %s is a prime number" % primeNumber)
