a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
        print(element)

array2 = []

for element in a:
    if element < 5:
        array2.append(element)
print(array2)

test = input("Input a number: ")
test = int(test)

array3 = []

for element in a:
    if element < test:
        array3.append(element)
print(array3)
