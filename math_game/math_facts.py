import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, project_root)
from math import floor
from pprint import pprint
from helpers.margin_separator_module import get_margin_separator
from math_game.math_gameboard import MathGameboard


## BEGIN
class MathFacts():
    """ The Math Facts game """

    __GAME_NAME = "Math Facts"
    __GAME_TIME = 30
    __ARITHMETIC_OPERATORS_LIST = ["+", "-", "x", "/"]

    def __init__(self, player=None):
        """ Creates the Math Facts game's start page """
        super().__init__()
        ## Private Constant
        self.__MARGIN_STR = get_margin_separator()
        ## Private
        self.__arithmetic_operator = "+" ## Default to Addition
        self.__arithmetic_operation = "Addition" 
        self.__max_operand = 1
        self.__operation_tple = (self.__arithmetic_operator, self.__arithmetic_operation, self.__max_operand)
        ## Protected
        self._player = player
        self._is_game_over = False
        self._final_score = 0 
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def is_game_over(self):
        return self._is_game_over
    

    @is_game_over.setter
    def is_game_over(self, is_game_over):
        self._is_game_over = is_game_over
        return
    

    def welcome_player(self, player=None):
        print(self.__MARGIN_STR)
        if(player):
            print("Hello, " + player.username + "! Welcome to " + self.__class__.__GAME_NAME + "!")
        else:
            print("Hello! Welcome to " + self.__class__.__GAME_NAME + "!")
        print(self.__MARGIN_STR)
        print("How many arithmetic equations can you solve in", self.__class__.__GAME_TIME, "seconds?")
        return
    

    ## Private
    def __select_arithmetic_operator(self):
        self.__arithmetic_operator = ""
        ERROR_MSG = "is not an arithmetic operator."
        while(self.__arithmetic_operator not in self.__class__.__ARITHMETIC_OPERATORS_LIST):
            try:
                print(self.__MARGIN_STR)
                print("To start, please press/enter an arithmetic operator:")
                print("Addition, Subtraction, Multiplication, or Division.")
                self.__arithmetic_operator = input("[+, -, x, /]: ").strip()
            except ValueError:
                if(self.__arithmetic_operator == ""):
                    print(f"{self.__MARGIN_STR}\nBlank space {ERROR_MSG}")
                else:
                    print(f"{self.__MARGIN_STR}\n{self.self._arithmetic_operator} {ERROR_MSG}")
            else:
                if(self.__arithmetic_operator == ""):
                    print(f"{self.__MARGIN_STR}\nBlank space {ERROR_MSG}")
                elif(self.__arithmetic_operator not in self.__class__.__ARITHMETIC_OPERATORS_LIST):
                    print(f"{self.__MARGIN_STR}\n{self.__arithmetic_operator} {ERROR_MSG}")
        return self.__arithmetic_operator
    

    ## Private
    def __select_max_operand(self):
        self.__max_operand = 0
        ERROR_MSG = "is not a whole number from 1 through 100."
        while(self.__max_operand < 1 or self.__max_operand > 100):
            try:
                print(self.__MARGIN_STR)
                print("Next, please enter a whole number from 1 through 100 (inclusive) for the maximum operand value.")
                self.__max_operand = int(floor(float(
                    input("Enter max operand: [1 through 100] ").strip()
                )))
            except ValueError:
                print(f"{self.__MARGIN_STR}\n{self.__max_operand} {ERROR_MSG}")
            else:
                if(self.__max_operand < 1 or self.__max_operand > 100):
                    print(f"{self.__MARGIN_STR}\n{self.__max_operand} {ERROR_MSG}")
        return self.__max_operand
    

    def __get_arithmetic_operation_name(self, arithmetic_operator="+"):
        if(arithmetic_operator == "+"):
            self.__arithmetic_operation = "Addition"
        elif(arithmetic_operator == "-"):
            self.__arithmetic_operation = "Subtraction"
        elif(arithmetic_operator == "x"):
            self.__arithmetic_operation = "Multiplication"
        elif(arithmetic_operator == "/"):
            self.__arithmetic_operation = "Division"
        return self.__arithmetic_operation    
    

    def get_operation_tple(self):
        arithmetic_operator = self.__select_arithmetic_operator()
        if(arithmetic_operator):
            operation_name = self.__get_arithmetic_operation_name(arithmetic_operator=arithmetic_operator)
            max_operand = self.__select_max_operand()
        if(max_operand and operation_name):
            self.__operation_tple = (self.__arithmetic_operator, self.__arithmetic_operation, 
                                     self.__max_operand)
        return self.__operation_tple


    def introduce_game(self, operation_tple=("+", "Addition", 1)):
        self.__arithmetic_operator, self.__arithmetic_operation, self.__max_operand = operation_tple
        print(self.__MARGIN_STR)
        print("\n* You selected " + self.__arithmetic_operation + ": '" + self.__arithmetic_operator 
              + "' with a max operand number of " + str(self.__max_operand) + ".")
        print("* You have " + str(self.__class__.__GAME_TIME) + " SECONDS on the clock to solve as many " + 
              self.__arithmetic_operation + " equations as you can.")
        print("* Type an answer and press ENTER to submit.")
        print("* For DIVISION: Round your answer to 2 decimal places.")
        print("* Type 'zzz' at the prompt and press ENTER to quit.\n")
        return
    

    def create_gameboard(self, operation_tple=("+", "Addition", 1)):
        self.__arithmetic_operator, self.__arithmetic_operation, self.__max_operand = operation_tple
        gameboard = MathGameboard(game_name=self.__class__.__GAME_NAME, 
                                  game_time=self.__class__.__GAME_TIME, 
                                  arithmetic_operator=self.__arithmetic_operator, 
                                  arithmetic_operation=self.__arithmetic_operation,
                                  max_operand=self.__max_operand)
        return gameboard
    

    def check_player_ready(self):
        player_answer = (
            input(f"Are you ready to start playing {self.__class__.__GAME_NAME}? [y/n] ")
        ).strip().lower()
        return player_answer
    

    def play_math_facts(self, player=None):
        ## While the game is not over:
        while(not self.is_game_over):
            self.welcome_player(player)
            arith_op, op_name, max_op_number = self.get_operation_tple()
            self.introduce_game(operation_tple=(arith_op, op_name, max_op_number))
            gameboard = self.create_gameboard(operation_tple=(arith_op, op_name, max_op_number))
            player_answer = self.check_player_ready()
            if(player_answer == "y" or player_answer == "yes"):
                if(player):
                    player._is_player_ready = True
                gameboard.start_game()
                ## If the game is over, but wasn't quit:
                if(gameboard._is_game_ended and not gameboard._was_game_quit):
                    if(player):
                        player.add_game_played_in_round(gameboard._game_id, gameboard._GAME_NAME, 
                                                        gameboard._game_date, gameboard._final_score)
                    user_answer = self.ask_play_again()
                    if(user_answer == ""):
                        continue
                    else:
                        gameboard.quit_game()
                        gameboard._was_game_quit = True
                        self._is_game_over = True
                else:
                    self._is_game_over = True
                    player_answer == "n"
                    break
            else:
                if(player):      
                    player._is_player_ready = False
                gameboard.quit_game()
                self._is_game_over = True
        else:
            if(player):      
                player.add_games_to_all_played_games_dict(player.games_played_in_round_dict)
                high_score = player.calc_high_score()
                print(self.__MARGIN_STR + "\nYour highest scoring game so far is:\n" + self.__MARGIN_STR)
                pprint(high_score)
            del gameboard
        return
    

    def ask_play_again(self):
        user_answer = (input("Want to play again? Press ENTER: [n/no to quit] ")).strip().lower()
        return user_answer
## END class


## To run `math_facts.py` stand-alone/individually
def main():
    game = MathFacts()
    game.play_math_facts()
    return


if(__name__ == "__main__"):
    main()