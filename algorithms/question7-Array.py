import unittest
"""
Given an array and an index,
find the product of the elements of the array except the element at that index.

"""


def selective_product(arr,index):
    prod = 1
    for i in range(len(arr)):
        if i != index :
            prod = prod * arr[i]
        else:
            continue
    return (prod)


class Test(unittest.TestCase):

    def setUp(self):
        self.arr =  [1, 4, 1, 3, 2, 1]

    def test1(self):
        self.assertEquals(selective_product(self.arr,1),6)


if __name__ == '__main__':
    unittest.main()
