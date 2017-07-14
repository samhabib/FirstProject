a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = 0
for elementsA in a:
    for elementsB in b:
        if elementsB == elementsA:
            if elementsA in c:
                d = 1
            else:
                c.append(elementsA)

print(c)
