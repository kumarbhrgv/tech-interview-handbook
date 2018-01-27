def longest_increasing_array(arr):
    """
    longest sub array in increasing order
    :param arr:
    :return: maximum length of sub array
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return 1
    end =1
    start = 0
    max_len = 1
    while end < len(arr):
        if arr[end] > arr[end - 1]:
            if end - start + 1 > max_len:
                max_len = end - start + 1
        else:
            start = end
        end += 1
    return max_len


print(longest_increasing_array([1,3,2,3,4,8,7,9]))
