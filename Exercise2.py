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