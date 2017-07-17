'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

palinTest = input("Type a word any word ")
palinTest = str(palinTest)

reverse = palinTest[::-1]

if palinTest == reverse:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

