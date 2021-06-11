from FoodTree import FoodTree
import os

class App:
    @classmethod
    def execute_app(self):
        self.__food_tree = FoodTree()
        self.__main(self)

    def __clear_console():
        os.system('clear')

    def __initial_message():
        print('Pense em um prato que gosta')

    def __new_food(self):
        new_food_plate = input('Qual prato você pensou?\n> ')
        new_food_type = input(f'{new_food_plate} é ____ mas {self.__food_tree.current_node.value} não.\n> ')

        return self.__food_tree.create_node(new_food_type, new_food_plate)

    def __main(self):
        self.__initial_message()

        while True:
            user_answer = int(input(f'É {self.__food_tree.current_node.value}?\n> '))

            if user_answer:
                if self.__food_tree.current_node_have_child():
                    self.__food_tree.current_node_walk_to_right()
                else:
                    self.__clear_console()
                    print('Acertei!')
                    self.__initial_message()
                    self.__food_tree.reset_current_node()
            else:
                if self.__food_tree.current_node_have_child():
                    self.__food_tree.current_node_walk_to_left()
                else:
                    self.__new_food(self)

                    self.__food_tree.reset_current_node()
                    self.__clear_console()

App.execute_app()