from Node import Node

class FoodTree:
    def __init__(self):
        self.__root_node = Node('Massa', Node('Lasanha'), Node('Bolo de chocolate'))
        self.__current_node = self.__root_node

    @property
    def current_node(self):
        return self.__current_node

    def reset_current_node(self):
        self.__current_node = self.__root_node

    def current_node_walk_to_right(self):
        self.__current_node = self.__current_node.right

    def current_node_walk_to_left(self):
        self.__current_node = self.__current_node.left

    def current_node_have_child(self):
        return self.__current_node.right or self.__current_node.left 

    def create_node(self, value, right_value):
        left_value = self.__current_node.value

        self.__current_node.value = value
        self.__current_node.right = Node(right_value)
        self.__current_node.left = Node(left_value)