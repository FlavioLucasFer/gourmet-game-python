class Node:
    def __init__(self, value, right_node = None, left_node = None):
        self.__value = value
        self.__right_node = right_node
        self.__left_node = left_node

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value

    def get_right_node(self):
        return self.__right_node

    def set_right_node(self, right_node):
        self.__right_node = right_node
    
    def get_left_node(self):
        return self.__left_node

    def set_left_node(self, left_node):
        self.__left_node = left_node

    def have_right_node(self):
        if self.__right_node is not None:
            return True
        return False

    def have_left_node(self):
        if self.__left_node is not None:
            return True
        return False