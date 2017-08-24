'''Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
to largest) and another number. The function decides whether or not the given number is inside the list and returns
/(then prints) an appropriate boolean.

Extras:
    Use binary search.
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


def linear(sample, target):

    if target < sample[0] or target > sample[len(sample)-1]:
        return False

    for x in range(0, len(sample)):
        if target < int(sample[x]):
            return False
        if sample[x] == target:
            return True
    return False

def binarysearch(sample, target):

    lo = 0
    hi = len(sample)-1
    mid = (hi + lo) // 2

    while lo <= hi:
        if target == sample[mid]:
            return True
        elif target > sample[mid]:
            if (lo == mid) and (hi == lo+1):
                break
            lo = mid
            mid = (hi + lo) // 2
        elif target < sample[mid]:
            if (hi == mid) and (lo == hi - 1):
                break
            hi = mid
            mid = (hi + lo) // 2
        print(hi, lo, mid)

    if sample[hi] == target or sample[lo] == target:

        return True

    else:

        return False


temp = input("Give me a number and I shall see if its in the list: ")
temp = int(temp)

if linear(a, temp):
    print("Wow I can't believe %s was in the list!!" % temp)

else:
    print("WRONG!")

if binarysearch(a, temp):
    print("Wow I can't believe %s was in the list!! BS Style" % temp)

else:
    print("WRONG! BS Style")
