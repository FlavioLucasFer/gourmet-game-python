
class Node():
    def __init__(self, value, right = None, left = None):
        self.__value = value
        self.__right = right
        self.__left = left

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right
    
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    def have_right(self):
        if self.__right is not None:
            return True
        return False

    def have_left(self):
        if self.__left is not None:
            return True
        return False