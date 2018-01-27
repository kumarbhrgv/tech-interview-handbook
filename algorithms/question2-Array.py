import unittest


def isSubsetSum(set, n, sum):
    """
    Determine if set contains subset which has desired sum.
    :param set: list of values
    :param n: length of set
    :param sum: intended sum of values
    :return: True or False
    """
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n - 1] > sum:
        return isSubsetSum(set, n - 1, sum);
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


class TestSubsetSum(unittest.TestCase):
    def setUp(self):
        self.arr  = [1, 2, 3, 4, 5, 6, 7]
        self.sum = 6

    def test(self):
        self.assertEqual(isSubsetSum(self.arr,len(self.arr),self.sum),True)
        self.sum = 7
        self.assertEqual(isSubsetSum(self.arr, len(self.arr), self.sum), True)
        self.sum = 10
        self.assertEqual(isSubsetSum(self.arr, len(self.arr), self.sum), True)
        self.sum = 0
        self.assertEqual(isSubsetSum(self.arr, len(self.arr), self.sum), True)

    #def test(self):
        #self.assertIsNotNone(isSubsetSum())
