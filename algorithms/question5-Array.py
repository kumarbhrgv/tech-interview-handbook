"""
Given array of arrays, sort them in ascending order.
Merge sort
"""

def merge_sort(a,low,high):
    """
    subroutine to split and merge
    :param a:
    :param low:
    :param high:
    :return:
    """
    print(low,high)
    if high == low:
        return [a[low]]
    else:
        mid = (low + high)//2
        left = merge_sort(a,low,mid)
        right = merge_sort(a,mid+1,high)
        return merge(left,right)

def merge(left,right):
    """
    merge two arrays
    :param left:
    :param right:
    :return:
    """
    print(left,right)
    i_right = 0
    res = []
    i_left= 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            res.append(left[i_left])
            i_left +=1
        else:
            res.append(right[i_right])
            i_right += 1
    print(res)
    while i_left < len(left):
        res.append(left[i_left])
        i_left += 1
    while i_right < len(right):
        res.append(right[i_right])
        i_right += 1
    return res


print(merge_sort([1,4,3,2],0,3))
