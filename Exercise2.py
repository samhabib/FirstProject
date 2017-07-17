'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''



TestNum = input("Give me a number and I will tell you if its ood or even :")
TestNum = int(TestNum)
if TestNum % 2 == 1:
    print("The number you inputted is Odd")
elif TestNum % 4 == 0:
    print("The number you inputted is Even and is divisible by 4")
elif TestNum % 2 == 0:
    print("The number you inputted is Even")

num = input("Give me another number :")

check = input("Give me ANOTHER number to see if we can divide it evenly into the previous number :")

num = int(num)
check = int(check)

if num % check == 0:
    print("%s divides into %s evenly" % (num, check))

elif num % check != 0:
    print("%s does not divide into %s evenly" % (num, check))