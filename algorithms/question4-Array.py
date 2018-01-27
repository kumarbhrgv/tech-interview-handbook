import math
"""
Implement a circular buffer using an array.
Circular buffer = a data structure that used a array as if it were connected end-to-end

"""


class CircularBuffer(object):

    def __init__(self, maxlen=10):
        """
        CircularBuffer, initialize length and empty array
        :param maxlen:
        """
        self.maxlen = maxlen+1
        self.array = [None] * (maxlen+1)
        self.read_pos = 0
        self.write_pos = 0

    def read(self):
        """
        read an element, update read_pos
        :return:
        """
        if self.read_pos != self.write_pos:
            return_val = self.array[self.read_pos]
            self.read_pos = (self.read_pos + 1) % self.maxlen
            return return_val
        else:
            return -1

    def write(self,val):
        """
        write value at write_pos, update write_pos
        :param val:
        :return: returns -1 on failure
        """
        self.print()
        if (self.write_pos+1) % self.maxlen != self.read_pos:
            self.array[self.write_pos] = val
            self.write_pos = (self.write_pos +1)%self.maxlen
            return self.write_pos
        else:
            print("Buffer full")
            return -1

    def print(self):
        print(self.array,self.read_pos,self.write_pos)


if __name__ == '__main__':

    buffer = CircularBuffer(maxlen=4)
    buffer.write("Hi1")
    buffer.write("Hi2")
    buffer.write("Hi3")
    buffer.write("Hi4")
    buffer.write("Hi5")
    print(buffer.read())
    print(buffer.read())
    buffer.write("Hi5")
    buffer.write("Hi6")
    buffer.write("Hi7")
    buffer.write("Hi8")

