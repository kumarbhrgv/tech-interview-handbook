import math
"""
Paginate an array with constraints, such as skipping certain items.

example:
dividing large lists of items into pages. The user is shown one page at a time and can navigate to other pages. 
"""


class ArrayPaginator(object):
    def __init__(self,arr,page_size):
        """

        :param arr: array/list
        :param page_size: page_size - int
        """
        self.array = arr
        self.curr_page = 0
        self.page_size = page_size
        self.total_pages = len(self.array)//page_size +1

    def get_next_page(self):
        """
        returns next page
        :return: return next page
        """
        index = self.curr_page
        if index + 1 < self.total_pages :
            self.curr_page +=1
            return self.array[index*self.page_size:self.curr_page*self.page_size]
        else :
            return -1

    def has_next_page(self):
        """
        check for next page
        :return:
        """
        index = self.curr_page + 1
        if index < self.total_pages:
            return True
        else:
            return False


if __name__ == "__main__":
    arrayPaginator = ArrayPaginator([1,2,3,4,5,6],2)
    while arrayPaginator.has_next_page():
        print(arrayPaginator.get_next_page())
