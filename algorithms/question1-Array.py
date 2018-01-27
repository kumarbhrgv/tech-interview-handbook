import unittest

"""
Iterator class for list
Implemented has_next(),next(),remove
"""


class ArrayIterator:
    def __init__(self,array):
        """

        :type array: list of elements
        """
        self.array = array
        self.array_length = len(array)
        self.curr = array[0]
        self.curr_index = 0

    def get_curr_index(self):
        """
        current index pointed by iterator
        :return:
        """
        return self.curr_index

    def get_curr(self):
        """
        current element pointed by iterator
        :return:
        """
        return self.curr

    def next(self):
        """
        next value of iterator
        :return:
        """
        if self.has_next():
            self.curr_index = self.curr_index +1
            return self.array[self.curr_index]
        else:
            return -1

    def has_next(self):
        """
        check if iterator has pointed to end of the list
        :return:
        """
        index = self.curr_index + 1
        if index >= self.array_length:
            return False
        else:
            return True

    def remove_next(self):
        """
        remove next element
        :return: -1 if cannot remove
        """
        return self.array.remove(self.next())

    def remove(self, toremove):
        """
        -1 if cannot remove or None if first element is removed
        :param toremove:
        :return: -1 if cannot remove or None if first element is removed
        """
        for i in range(0,len(self.array)):
            element = self.array[i]
            if toremove == element:
                self.array.slice(i,i+1)
                return None
        return -1


class TestArrayIterator(unittest.TestCase):
    def setUp(self):
        self.x = [1, 2, 3, 4, 5, 6, 7]
        self.array_iterator = ArrayIterator(self.x)

    def test(self):
        self.assertEqual(self.array_iterator.get_curr_index(), 0)
        self.assertEqual(self.array_iterator.next(), 2)
        self.assertEqual(self.array_iterator.get_curr_index(), 1)
        self.assertEqual(self.array_iterator.has_next(), True)
        self.assertEqual(self.array_iterator.array_length, 7)
        self.assertEqual(self.array_iterator.remove_next(), None)
        self.assertEqual(self.array_iterator.remove(10), -1)
        self.assertEqual(self.array_iterator.has_next(), True)


if __name__ == '__main__':
    unittest.main()
