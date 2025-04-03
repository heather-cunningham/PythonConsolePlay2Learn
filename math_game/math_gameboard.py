from random import randint
from gameboard import Gameboard
from helpers.countdown_timer import CountdownTimer
from helpers.margin_separator_module import get_margin_separator
from helpers.prompt_player import GOODBYE_MSG

## BEGIN
class MathGameboard(Gameboard):
    """ The gameboard for Math Facts. """


    def __init__(self, game_name="Math Facts", game_time=30, arithmetic_operator="+", 
                 arithmetic_operation="Addition", max_operand=1):
        """ Creates a gameboard for the Math Facts arithmetic game and game play.
         
        Keyword arguments: `word_length` (int) -- The number of characters for the length of the words from which
                                                  to make anagrams.  Defaults to 5.
                            `game_time` (int) -- The number of seconds for the game interval and its timer.                        
        """
        super().__init__(game_name=game_name)
        ## Constants
        self.__MARGIN_STR = get_margin_separator()
        self._GAME_NAME = game_name
        self._GAME_TIME = game_time
        ## Protected
        self._game_id = 0
        self._game_date = 0
        self._is_game_ended = False
        self._was_game_quit = False
        self._final_score = 0
        ## Private
        self.__arithmetic_operator = arithmetic_operator
        self.__arithmetic_operation = arithmetic_operation 
        self.__max_operand = max_operand
        self.__equation = ""
        self.__user_answer = 0
        self.__user_score = 0
        self.__is_correct_answer = False
        self.__timer = CountdownTimer(seconds=self._GAME_TIME)


    def __get_random_integer(self, max_operand=1):
        return randint(0, max_operand)
    

    def __set_next_equation(self):
        operand1 = self.__get_random_integer(max_operand=self.__max_operand)
        operand2 = self.__get_random_integer(max_operand=self.__max_operand)
        if(self.__arithmetic_operation == "Division"):
            while(operand2 == 0):
                operand2 = self.__get_random_integer(max_operand=self.__max_operand)
        self.__equation = f"{str(operand1)} {self.__arithmetic_operator} {str(operand2)} = "
        return self.__equation
    

    def __format_number(self, number):
        if (number.is_integer()):
            try:
                number = int(number)
                return number
            except ValueError:
                print("Could not parse number,", number, ", to an integer.")
        else:
            try:
                number = float(number) 
                number = round(number, 2)
                return number
            except ValueError:
                print("Could not parse number,", number, ", to a float.")
        

    ## Protected
    ## @override
    def _start_game_timer(self):
        return self.__timer.start_timer()
    

    ## @override
    def start_game(self):
        Gameboard.game_name = self._GAME_NAME
        self._game_id = Gameboard._generate_game_id(Gameboard.game_name)
        self._game_date = Gameboard._set_game_date()
        print(f"* You have {self._GAME_TIME} seconds.\n")
        self._start_game_timer()
        self._play_round()
        return
    

    ## Protected
    ## @override
    def _ask_question(self, equation="1 + 1 = "):
        is_valid_num = False
        user_solution = None
        self.__equation = equation
        print("Enter an answer: [type 'zzz' to quit]")
        while(not is_valid_num):
            user_solution = input(self.__equation).strip().lower()
            if(user_solution == "zzz"):
                return user_solution
            try:
                user_solution = float(user_solution)
                is_valid_num = True
                return user_solution
            except ValueError:
                print(f"{self.__MARGIN_STR}\nAnswers must be numbers.\n{self.__MARGIN_STR}")
        return user_solution


    ## Protected
    ## @override
    def _check_for_correct_answer(self, user_solution):
        if(user_solution is not None):
            try:
                operand1 = int(self.__equation.split(" ")[0])
                operand2 = int(self.__equation.split(" ")[2])
            except ValueError:
                print(f"Could not parse the operands:", operand1, ",", operand2)
            if(self.__arithmetic_operation.title() == "Addition"):
                if(user_solution == (operand1 + operand2)):
                    self.__is_correct_answer = True
                    self._increment_score()
                    return self.__is_correct_answer
                else:
                    self.__is_correct_answer = False
                    return self.__is_correct_answer
            elif(self.__arithmetic_operation.title() == "Subtraction"):
                if(user_solution == (operand1 - operand2)):
                    self.__is_correct_answer = True
                    self._increment_score()
                    return self.__is_correct_answer
                else:
                    self.__is_correct_answer = False
                    return self.__is_correct_answer
            elif(self.__arithmetic_operation.title() == "Multiplication"):
                if(user_solution == (operand1 * operand2)):
                    self.__is_correct_answer = True
                    self._increment_score()
                    return self.__is_correct_answer
                else:
                    self.__is_correct_answer = False
                    return self.__is_correct_answer
            elif(self.__arithmetic_operation.title() == "Division"):
                if(user_solution == self.__format_number(operand1 / operand2)):
                    self.__is_correct_answer = True
                    self._increment_score()
                    return self.__is_correct_answer
                else:
                    self.__is_correct_answer = False
                    return self.__is_correct_answer
            else:
                print("Invalid operation:", self.__arithmetic_operation, "is not an arithmetic operation")
                self.__is_correct_answer = False
                return self.__is_correct_answer
        else:
            self.__is_correct_answer = False
        return self.__is_correct_answer
         

    ## Protected
    ## @override
    def _increment_score(self):
        self.__user_score += 1
        return self.__user_score
    

    ## Protected
    ## @override
    def _show_user_display(self):
        if(self.__timer is not None and self.__timer.seconds > 0):
            print(f"\nYou have {self.__timer.seconds} seconds left.")
        else:
            print(f"\nYou have 0 seconds left.")
        print(f"Your score: {self.__user_score}\n")
        return
    

    ## Protected 
    ## @override
    def _play_round(self):
        while(self.__timer is not None and self.__timer.seconds > 0):
            self.__equation = self.__set_next_equation()
            is_correct = False
            while (not is_correct and self.__timer is not None and self.__timer.seconds > 0):
                self.__user_answer = self._ask_question(equation=self.__equation)
                if ((str(self.__user_answer)).strip().lower() == "zzz"):
                    self.quit_game()
                    return
                is_correct = self._check_for_correct_answer(self.__user_answer)
                if(not is_correct):
                    self.__user_answer = self.__format_number(self.__user_answer)
                    print(f"\n{self.__user_answer} is not correct.  Try again!\n")
            else:
                self.__user_answer = self.__format_number(self.__user_answer)
                print(f"\n{self.__user_answer} is correct!")
            self._show_user_display()
        else:
            self._end_game()
                
    
    ## Protected 
    ## @override
    def _reset_game(self):
        self._is_game_ended = True
        self.__timer = None
        self.__equation = ""
        self.__user_score = 0
        self.__user_answer = 0
        self.__is_correct_answer = False
        return
    
    
    ## Protected 
    ## @override
    def _stop_game_timer(self):
        return self.__timer.stop_timer()
    

    ## @override
    def quit_game(self):
        print(GOODBYE_MSG)
        if(self.__timer is not None and self.__timer.seconds > 0):
            self._stop_game_timer()
        self._reset_game()
        self._was_game_quit = True
        return


    ## Protected 
    ## @override
    def _end_game(self):
        print("GAME OVER:")
        print("Time's up!!!")
        if(self.__timer is None or self.__timer.seconds <= 0):
            print("Sorry, you didn't get that last one in on time.")
        elif(self.__timer is not None or self.__timer.seconds > 0):
            self._stop_game_timer()
        #
        if(self.__user_score > 0):
            print("You solved", self.__user_score, self.__arithmetic_operation, "equations!")
        else:
            print("Aww, you didn't solve any", self.__arithmetic_operation, 
                    " equations this game. Better luck next time!")
        self._final_score = self.__user_score
        self._reset_game()
        return
## END class