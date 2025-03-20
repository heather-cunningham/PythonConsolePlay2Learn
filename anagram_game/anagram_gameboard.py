import os
import json
import random
from gameboard import Gameboard
from helpers.margin_separator_module import get_margin_separator
from helpers.countdown_timer import CountdownTimer


## BEGIN
class AnagramGameboard(Gameboard):
    """ The gameboard for Anagram Hunt. """


    def __init__(self, word_length=5):
        """ Creates a gameboard for the Anagram Hunt game and game play.
         
        Keyword arguments: `word_length` (int) -- The number of characters for the length of the words from which
                                                  to make anagrams.  Defaults to 5. 
        """
        super().__init__()
        ## Constants
        self._MARGIN_STR = get_margin_separator()
        self.__GAME_NAME = "Anagram Hunt"
        self._GAME_TIME = 60
        ## Protected
        self._game_id
        self._game_date
        self._is_game_ended = False
        self._was_game_quit = False
        ## Private
        self.__word_length = word_length
        self.__data = None
        self.__list_of_word_lists = []
        self.__word_list = []
        self.__anagram_word = ""
        self.__user_answer = ""
        self.__user_score = 0
        self.__is_correct_answer = False
        self.__correct_guesses_list = []
        self.__timer = CountdownTimer(seconds=self._GAME_TIME)
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return


    @property
    def _game_id(self):
        return self.__game_id
    

    @_game_id.setter
    def _game_id(self, game_id):
        self.__game_id = game_id
        return


    @property
    def _game_date(self):
        return self.__game_date
    

    @_game_date.setter
    def _game_date(self, game_date):
        self.__game_date = game_date        
        return

    ## Private
    def __get_abs_filepath(self, rel_filepath_str):
        folder_name = os.path.dirname(os.path.abspath(__file__))
        path_parts_list = rel_filepath_str.split("/") 
        return os.path.join(folder_name, *path_parts_list) 


    ## Private
    def __get_json_data(self):
        rel_filepath_str = "./data/anagrams.json"
        data_abs_filepath = self.__get_abs_filepath(rel_filepath_str)
        with open(data_abs_filepath) as file:
            self.__data = json.load(file)
        return self.__data


    ## Private
    ## Set/get the list of multiple word lists of this character length 
    def __set_list_of_word_lists(self):
        word_len_str = str(self.__word_length) 
        self.__data = self.__get_json_data()
        if(self.__data):
            if(word_len_str in self.__data):
                self.__list_of_word_lists = self.__data[word_len_str]
                return self.__list_of_word_lists
            else:
                print("!!!!", word_len_str, "chars word length not found in data.")
        else:
            print("!!!! Data is empty or NOT FOUND")
        return self.__list_of_word_lists


    ## Private
    ## Set/get 1 random list out of the list of multiple word lists of this character length
    def __set_word_list(self):
        if(self.__list_of_word_lists):
            ## Get a random list out of the Parent list of word lists
            self.__word_list = random.choice(self.__list_of_word_lists)
            if(self.__word_list):
                self.__remove_word_list()
                return self.__word_list
            else:
                print("!!!! Word_list is empty or not found.")
        else:
            print("!!!! Parent list of word lists is empty or not found.")
        return self.__word_list
    

    ## Private
    ## Set/get 1 random word out of the 1 word list of this character length
    def __set_anagram_word(self):
        if(self.__word_list):
            self.__anagram_word = random.choice(self.__word_list)
            if(self.__anagram_word):
                self.__remove_word(self.__anagram_word)
                return self.__anagram_word
            else:
                print("!!!! Anagram_word is empty or not found.")    
        else:
            print("!!!! Word_list is empty or not found.")
        return self.__anagram_word


    ## Private
    ## Remove this word list form the List of word lists of this character length
    def __remove_word_list(self):
        if(self.__word_list in self.__list_of_word_lists):
            self.__list_of_word_lists.remove(self.__word_list)
        else:
            print("Word List NOT FOUND in List of Word Lists.")
        return


    ## Private
    ## Remove this word from the current word list
    def __remove_word(self, word_to_remove):
        if(word_to_remove in self.__word_list):
            self.__word_list.remove(word_to_remove)
        else:
            print(word_to_remove, "NOT FOUND in Word List:", self.__word_list)
        return
    

    ## Protected
    ## @override
    def _start_game_timer(self):
        return self.__timer.start_timer() 


    ## @override
    def start_game(self):
        Gameboard.game_name = self.__GAME_NAME
        self._game_id = Gameboard._generate_game_id(Gameboard.game_name)
        self._game_date = Gameboard._set_game_date()
        self.__set_list_of_word_lists()
        self.__set_word_list()
        self.__set_anagram_word()
        print(f"* You have {self._GAME_TIME} seconds.\n")
        self._start_game_timer()
        self._play_game()
        return
    

    ## Protected
    ## @override
    def _ask_question(self, word_to_anagram):
        word_to_anagram = word_to_anagram.upper()
        print("The word is:", word_to_anagram)
        print(f"There {'is' if len(self.__word_list) == 1 else 'are'} "
              f"{len(self.__word_list)} anagram{'s' if len(self.__word_list) != 1 else ''} "
              f"remaining for: {word_to_anagram}.")
        guess = input("Enter a guess: [type 'zzz' to quit] ")
        return guess
    

    ## Protected
    ## @override
    def _check_for_correct_answer(self, guess):
        guess = guess.lower()
        if(guess == self.__anagram_word): ## Guessed same word as in the question
            print("\n* You can't guess: " + self.__anagram_word.title() 
                  + ".  It's the same word as the question.  Please, try again.\n")
            self.__is_correct_answer = False
            return self.__is_correct_answer
        elif(guess in self.__correct_guesses_list): ## Guessed same answer as guessed already 
            print("\n* You've guessed: " + guess.title() + " already.\n")
            self.__is_correct_answer = False
            return self.__is_correct_answer
        elif(guess in self.__word_list): ## Guessed correctly
            print("\n*", guess.title(), "is correct!\n")
            self.__remove_word(guess)
            self._increment_score()
            self.__is_correct_answer = True
            self.__correct_guesses_list.append(guess)
            return self.__is_correct_answer    
        else: ## Guessed wrong
            print("\n* " + guess.title() + " is not a valid anagram of: " + self.__anagram_word.upper() 
                  + ".  Please, try again.\n")
            self.__is_correct_answer = False
        return self.__is_correct_answer
    

    ## Protected
    ## @override
    def _increment_score(self):
        self.__user_score += 1
        return self.__user_score
    

    ## Private
    def __show_user_display(self):
        if(self.__timer is not None and self.__timer.seconds > 0):
            print("Your score:", self.__user_score)
            print("* You've guessed correctly:", self.__correct_guesses_list)
            if(len(self.__word_list) > 0):
                print(f"* There {'is' if len(self.__word_list) == 1 else 'are'} "
                      f"{len(self.__word_list)} anagram{'s' if len(self.__word_list) != 1 else ''} "
                      f"left to guess.")
            else:
                print(f"* YOU GUESSED ALL THE ANAGRAMS FOR {self.__anagram_word.title()}. YAY!!! :)")
            print("* You have", self.__timer.seconds, "seconds left.\n")
        return
    

    ## Protected 
    ## @override
    def _play_game(self):
        ## While there is a list of word_lists of this char length, and still time:
        while (len(self.__list_of_word_lists) > 0 and self.__timer is not None and self.__timer.seconds > 0):
            ## While there are words still in this word_list of this char length, and still time:
            while (len(self.__word_list) > 0 and self.__timer is not None and self.__timer.seconds > 0):
                self.__user_answer = self._ask_question(self.__anagram_word)
                if (self.__user_answer.lower() == "zzz"):
                    self.quit_game()
                    return
                is_correct = self._check_for_correct_answer(self.__user_answer)
                self.__show_user_display()
                while (not is_correct and self.__timer is not None and self.__timer.seconds > 0):
                    self.__user_answer = self._ask_question(self.__anagram_word)
                    if (self.__user_answer.lower() == "zzz"):
                        self.quit_game()
                        return
                    is_correct = self._check_for_correct_answer(self.__user_answer)
                    self.__show_user_display()
                else:
                    if(self.__timer is None or self.__timer.seconds < 0):
                        break
            else: ## Get the next word_list form the lists of lists of this char length:
                if(self.__timer is not None and self.__timer.seconds > 0):
                    self.__set_word_list()
                    self.__set_anagram_word()
                    self.__correct_guesses_list = []
        else: ## There're no word lists left of this char length, or no more time:
            self._end_game()
        return
    

    ## Protected 
    ## @override
    def _reset_game(self):
        self._is_game_ended = True
        self.__timer = None
        self.__word_list = []
        self.__list_of_word_lists = []
        self.__user_score = 0
        self.__user_answer = ""
        self.__correct_guesses_list = []
        self.__is_correct_answer = False
        return   
    

    ## Protected 
    ## @override
    def _stop_game_timer(self):
        return self.__timer.stop_timer()


    ## @override
    def quit_game(self):
        print("Thanks for playing! TTFN (ta ta for now)!")
        if(self.__timer is not None and self.__timer.seconds > 0):
            self._stop_game_timer()
        self._reset_game()
        self._was_game_quit = True
        return   
    

    ## Protected 
    ## @override
    def _end_game(self):
        if(self.__timer is not None and self.__timer.seconds > 0):
            self._stop_game_timer()
            print("You guessed all " + str(self.__user_score) + " anagrams for " + str(self.__word_length) 
                  + "-letter words before the " + str(self._GAME_TIME) + " seconds expired!!!")
        else:
            print("Time's up!!!")
            print("Sorry, you didn't get that last one in on time.")
        if(self.__user_score > 0):
            print(f"You guessed {self.__user_score} anagrams for {self.__word_length}-letter words!")
            print("Good for you! :)  Hooray!!!")
        elif(self.__user_score == 0):
            print("Aww, you didn't guess any anagrams for " + str(self.__word_length) + "-letter words." 
                  + "  Better luck next time!")
        Gameboard._final_score = self.__user_score
        self._reset_game()
        return
## END class
