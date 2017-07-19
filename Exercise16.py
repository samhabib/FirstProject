'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random
import string

strength = input("Type in 'weak' or 'strong' for a password of that level: ")

if strength == 'weak':
    a = ['hello', 'temp', 'password', 'weak', 'sauce', 'words', 'television', 'Dora', 'texture']
    temp = a[random.randint(0,8)]
    print(temp)

elif strength == 'strong':

    N = 7
    temp = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=N))
    print(temp)

else:
    print("Incorrect input ")