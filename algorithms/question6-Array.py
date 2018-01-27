"""
Given an array of integers, print out a histogram using the said array;
include a base layer (all stars)
ex: [5, 4, 0, 3, 4, 1]
*
**  *
** **
** **
** ***
******
"""

def printHist(arr):
    """
    print histogram for array
    :param arr:
    :return:
    """
    for i in range(max(arr)):
        max_val = max(arr)
        for j in range(len(arr)):
            if arr[j] == max_val:
                print("*", end='  ')
                arr[j] -=1
            else:
                print(" ", end='  ')
        print()
    for i in range(len(arr)):
        print("*", end='  ')


if __name__ == '__main__':
    printHist([5,4,0,3,4,1])
