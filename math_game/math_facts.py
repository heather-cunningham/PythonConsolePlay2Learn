import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, project_root)
from player import Player
from helpers.margin_separator_module import get_margin_separator
from helpers.prompt_player_for_user import prompt_player_for_user_info, prompt_player_for_new_user_info


## BEGIN
class MathFacts():
    """ The Math Facts game """

    
    __GAME_TIME = 30
    __ARITHMETIC_OPERATORS_LIST = ["+", "-", "x", "/"]

    def __init__(self):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()
        self._MARGIN_STR = get_margin_separator()
        self._arithmetic_operator = "+" ## Default to Addition
        self._arithmetic_operation = "Addition" 
        self._max_operand = 1
        self._operation_tple = (self._arithmetic_operator, self._max_operand) 
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def is_game_over(self):
        return self._is_game_over
    

    @is_game_over.setter
    def is_game_over(self, is_game_over):
        self._is_game_over = is_game_over
        return
    

    def welcome_player(self, player):
        print(self._MARGIN_STR)
        print("Hello, " + player.username + "! Welcome to Math Facts!")
        print(self._MARGIN_STR)
        print("How many arithmetic equations can you solve in", self.__class__.__GAME_TIME, "seconds?")
        print(self._MARGIN_STR)
        return
    

    def select_arithmetic_operator(self):
        self._arithmetic_operator = ""
        self._max_operand = 0
        ERROR_MSG = "is not an arithmetic operator. Please, press: " + self.__class__.__ARITHMETIC_OPERATORS_LIST
        while(self._arithmetic_operator not in self.__class__.__ARITHMETIC_OPERATORS_LIST):
            try:
                print("To start, please press/enter an arithmetic operator --")
                print("Addition, Subtraction, Multiplication, or Division:")
                self._arithmetic_operator = input("[+, -, x, /]: ").strip()
                self._max_operand = self.select_max_operand()
            except ValueError:
                print(f"{self._MARGIN_STR}\n{self.self._arithmetic_operator} {ERROR_MSG}\n{self._MARGIN_STR}")
            else:
                if(self._arithmetic_operator not in self.__class__.__ARITHMETIC_OPERATORS_LIST):
                    print(f"{self._MARGIN_STR}\n{self.self._arithmetic_operator} {ERROR_MSG}\n{self._MARGIN_STR}")
                else:
                    self._max_operand = self.select_max_operand()
        self._operation_tple = (self._arithmetic_operator, self._max_operand)
        return self._operation_tple
    

    def select_max_operand(self):
        self._max_operand = 0
        ERROR_MSG = "is not a number from 1 through 100."
        while(self._max_operand < 1 or self._max_operand > 100):
            try:
                self._max_operand = int(input("To start, please enter a max operand number from 1 through 100: "))
            except ValueError:
                print(f"{self._MARGIN_STR}\n{self._max_operand} {ERROR_MSG}\n{self._MARGIN_STR}")
            else:
                if(self._max_operand < 1 or self._max_operand > 100):
                    print(f"{self._MARGIN_STR}\n{self._max_operand} {ERROR_MSG}\n{self._MARGIN_STR}")
        return self._max_operand
    

    def introduce_game(self, _operation_tple=("+", 1)):
        self._arithmetic_operator, self._max_operand = _operation_tple
        #
        if(self._arithmetic_operator == "+"):
            self._arithmetic_operation = "Addition"
        elif(self._arithmetic_operator == "-"):
            self._arithmetic_operation = "Subtraction"
        elif(self._arithmetic_operator == "x"):
            self._arithmetic_operation = "Multiplication"
        elif(self._arithmetic_operator == "/"):
            self._arithmetic_operation = "Division"
        #
        print(self._MARGIN_STR)
        print("\n* You selected arithmetic operation: " + self._arithmetic_operation + ", " 
              + self._arithmetic_operator + ", with a max operand of: " + self._max_operand + ".")
        print("* You have " + self.__class__.__GAME_TIME + " SECONDS on the clock to solve as many " + 
              self._arithmetic_operation + " equations as you can with max operand number of: " 
              + self._max_operand + ".")
        print("* Type an answer and press ENTER to submit.")
        print("* Type 'zzz' at the prompt and press ENTER to quit.\n")
        return