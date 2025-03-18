import os
import json
import random
from pprint import pprint
from helpers.margin_separator_module import get_margin_separator
from helpers.countdown_timer import CountdownTimer


## BEGIN
class AnagramGameboard():
    """ The gameboard for Anagram Hunt. """


    def __init__(self, word_length=5):
        """ Creates a gameboard for the Anagram Hunt game and game play.
         
        Keyword arguments: `word_length` (int) -- The number of characters for the length of the words from which
                                                  to make anagrams.  Defaults to 5. 
        """
        super().__init__()
        ## Constants
        self._MARGIN_STR = get_margin_separator()
        self._GAME_TIME = 60
        ## Public
        self.is_game_ended = False
        self.was_game_quit = False
        ## Private
        self._word_length = word_length
        self._data = None
        self._list_of_word_lists = []
        self._word_list = []
        self._anagram_word = ""
        self._user_answer = ""
        self._user_score = 0
        self._is_correct_answer = False
        self._correct_guesses_list = []
        self._timer = CountdownTimer(seconds=self._GAME_TIME)
        ## Python convention of explicitly returning, even if empty, to mark the end of a method.
        return


    def _get_abs_filepath(self, rel_filepath_str):
        folder_name = os.path.dirname(os.path.abspath(__file__))
        path_parts_list = rel_filepath_str.split("/") 
        return os.path.join(folder_name, *path_parts_list) 


    def _get_json_data(self):
        rel_filepath_str = "./data/anagrams.json"
        data_abs_filepath = self._get_abs_filepath(rel_filepath_str)
        with open(data_abs_filepath) as file:
            self._data = json.load(file)
        return self._data


    ## Set/get the list of multiple word lists of this character length 
    def _set_list_of_word_lists(self):
        word_len_str = str(self._word_length) 
        self._data = self._get_json_data()
        if(self._data):
            if(word_len_str in self._data):
                self._list_of_word_lists = self._data[word_len_str]
                return self._list_of_word_lists
            else:
                print("!!!!", word_len_str, "chars word length not found in data.")
        else:
            print("!!!! Data is empty or NOT FOUND")
        return self._list_of_word_lists

    
    ## Set/get 1 random list out of the list of multiple word lists of this character length
    def _set_word_list(self):
        if(self._list_of_word_lists):
            ## Get a random list out of the Parent list of word lists
            self._word_list = random.choice(self._list_of_word_lists)
            if(self._word_list):
                self._remove_word_list()
                return self._word_list
            else:
                print("!!!! Word_list is empty or not found.")
        else:
            print("!!!! Parent list of word lists is empty or not found.")
        return self._word_list
    

    ## Set/get 1 random word out of the 1 word list of this character length
    def _set_anagram_word(self):
        if(self._word_list):
            self._anagram_word = random.choice(self._word_list)
            if(self._anagram_word):
                self._remove_word(self._anagram_word)
                return self._anagram_word
            else:
                print("!!!! Anagram_word is empty or not found.")    
        else:
            print("!!!! Word_list is empty or not found.")
        return self._anagram_word


    ## Remove this word list form the List of word lists of this character length
    def _remove_word_list(self):
        if(self._word_list in self._list_of_word_lists):
            self._list_of_word_lists.remove(self._word_list)
        else:
            print("Word List NOT FOUND in List of Lists:")
            print("Word List:\n", "-" * 25)
            pprint(self._word_list)
            print("List of Lists:\n", "-" * 25)
            pprint(self._list_of_word_lists)
        return


    ## Remove this word from the current word list
    def _remove_word(self, word_to_remove):
        if(word_to_remove in self._word_list):
            self._word_list.remove(word_to_remove)
        else:
            print(word_to_remove, "NOT FOUND in Word List:", self._word_list)
        return
    

    def _check_for_correct_answer(self, guess):
        guess = guess.lower()
        if(guess == self._anagram_word): ## Guessed same word as in the question
            print("\n* You can't guess: " + self._anagram_word.title() 
                  + ".  It's the same word as the question.  Please, try again.\n")
            self._is_correct_answer = False
            return self._is_correct_answer
        elif(guess in self._correct_guesses_list): ## Guessed same answer as guessed already 
            print("\n* You've guessed: " + guess.title() + " already.\n")
            self._is_correct_answer = False
            return self._is_correct_answer
        elif(guess in self._word_list): ## Guessed correctly
            print("\n*", guess.title(), "is correct!\n")
            self._remove_word(guess)
            self._increment_score()
            self._is_correct_answer = True
            self._correct_guesses_list.append(guess)
            return self._is_correct_answer    
        else: ## Guessed wrong
            print("\n* " + guess.title() + " is not a valid anagram of: " + self._anagram_word.upper() 
                  + ".  Please, try again.\n")
            self._is_correct_answer = False
        return self._is_correct_answer
    

    def _increment_score(self):
        self._user_score += 1
        return self._user_score
    

    def _show_user_display(self):
        if(self._timer is not None and self._timer.seconds > 0):
            print("Your score:", self._user_score)
            print("* You've guessed correctly:", self._correct_guesses_list)
            if(len(self._word_list) > 0):
                print(f"* There {'is' if len(self._word_list) == 1 else 'are'} "
                      f"{len(self._word_list)} anagram{'s' if len(self._word_list) != 1 else ''} "
                      f"left to guess.")
            else:
                print(f"* YOU GUESSED ALL THE ANAGRAMS FOR {self._anagram_word.title()}. YAY!!! :)")
            print("* You have", self._timer.seconds, "seconds left.\n")
        return


    def _ask_question(self, word_to_anagram):
        word_to_anagram = word_to_anagram.upper()
        print("The word is:", word_to_anagram)
        print(f"There {'is' if len(self._word_list) == 1 else 'are'} "
              f"{len(self._word_list)} anagram{'s' if len(self._word_list) != 1 else ''} "
              f"remaining for: {word_to_anagram}.")
        guess = input("Enter a guess: [type 'zzz' to quit] ")
        return guess
    

    def _play_game(self):
        ## While there is a list of word_lists of this char length, and still time:
        while (len(self._list_of_word_lists) > 0 and self._timer is not None and self._timer.seconds > 0):
            ## While there are words still in this word_list of this char length, and still time:
            while (len(self._word_list) > 0 and self._timer is not None and self._timer.seconds > 0):
                self._user_answer = self._ask_question(self._anagram_word)
                if (self._user_answer.lower() == "zzz"):
                    self.quit_game()
                    return
                is_correct = self._check_for_correct_answer(self._user_answer)
                self._show_user_display()
                while (not is_correct and self._timer is not None and self._timer.seconds > 0):
                    self._user_answer = self._ask_question(self._anagram_word)
                    if (self._user_answer.lower() == "zzz"):
                        self.quit_game()
                        return
                    is_correct = self._check_for_correct_answer(self._user_answer)
                    self._show_user_display()
                else:
                    if(self._timer is None or self._timer.seconds < 0):
                        break
            else: ## Get the next word_list form the lists of lists of this char length:
                if(self._timer is not None and self._timer.seconds > 0):
                    self._set_word_list()
                    self._set_anagram_word()
                    self._correct_guesses_list = []
        else: ## There're no word lists left of this char length, or no more time:
            self._end_game()
        return
    

    def start_game(self):
        self._set_list_of_word_lists()
        self._set_word_list()
        self._set_anagram_word()
        print(f"* You have {self._GAME_TIME} seconds.\n")
        self._timer.start_timer()
        self._play_game()
        return
    

    def _reset_game(self):
        self.is_game_ended = True
        self._timer = None
        self._word_list = []
        self._list_of_word_lists = []
        self._user_score = 0
        self._user_answer = ""
        self._correct_guesses_list = []
        self._is_correct_answer = False
        return   
    

    def quit_game(self):
        print("Thanks for playing! TTFN (ta ta for now)!")
        if(self._timer is not None and self._timer.seconds > 0):
            self._timer.stop_timer()
        self._reset_game()
        self.was_game_quit = True
        return   
    
    
    def _end_game(self):
        if(self._timer is not None and self._timer.seconds > 0):
            self._timer.stop_timer()
            print("You guessed all " + str(self._user_score) + " anagrams for " + str(self._word_length) 
                  + "-letter words before the " + str(self._GAME_TIME) + " seconds expired!!!")
        else:
            print("Time's up!!!")
            print("Sorry, you didn't get that last one in on time.")
            print(f"You guessed {self._user_score} anagrams for {self._word_length}-letter words!")
        print("Good for you! :)  Hooray!!!")
        self._reset_game()
        return
## END class
