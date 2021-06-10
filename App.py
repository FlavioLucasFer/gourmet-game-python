import os
from Food import Food
from Node import Node
from Tree import Tree


class App:
    @classmethod
    def execute_app(self):
        self.__food_tree = Tree(Node(Food('Massa'), Node(Food('Lasanha')), Node(Food('Bolo de chocolate'))))
        self.__main(self)

    def __clear_console():
        os.system('clear')

    def __initial_message():
        print('Pense em um prato que gosta')

    def __new_food(current_node):
        new_food_plate = input('Qual prato você pensou?\n> ')
        new_food_type = input(f'{new_food_plate} é ____ mas {current_node.get_value().get_name()} não.\n> ')
        
        current_node.set_left_node(Node(current_node.get_value()))
        current_node.set_right_node(Node(Food(new_food_plate)))
        current_node.set_value(Food(new_food_type))

        return current_node

    def __main(self):
        current_node = self.__food_tree.get_root_node()
        self.__initial_message()

        while True:
            user_answer = int(input(f'É {current_node.get_value().get_name()}?\n> '))

            if user_answer:
                if current_node.have_right_node():
                    current_node = current_node.get_right_node()
                else:
                    self.__clear_console()
                    print('Acertei!')
                    self.__initial_message()

                    current_node = self.__food_tree.get_root_node()
            else:
                if current_node.have_left_node():
                    current_node = current_node.get_left_node()
                    
                else:
                    current_node = self.__new_food(current_node)

                    current_node = self.__food_tree.get_root_node()
                    self.__clear_console()


App.execute_app()