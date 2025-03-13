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
        self.word_length = word_length
        self._margin_str = get_margin_separator()
        # self.player_ready = "n"
        self._data = None
        self._list_of_word_lists = []
        self._word_list = []
        self._anagram_word = ""
        self._user_answer = ""
        self._user_score = 0
        self._is_correct_answer = False
        self._correct_guesses_list = []
        self._timer = CountdownTimer(seconds=60)
        self._sorry_msg = "* Sorry, you didn't get that last one in on time.\n"
        ## Python convention of explicitly returning, even if empty, to mark the end of a method.
        return


    def introduce_game(self):
        print(self._margin_str)
        print("\n* You selected a word length of:", self.word_length, "characters.")
        print("* You have 60 SECONDS on the clock to enter as many anagrams as you can from a list of",
              self.word_length, "letter words, displayed one at a time.")
        print("* Answers MUST include all of the letters in the original word", 
              "to be considered a correct anagram.")
        print("* You MUST guess all of the correct anagrams for a displayed word", 
              "before progressing to the next in the list.")
        print("* Type a guess and press ENTER to submit an answer.\n")
        return


    def get_json_data(self):
        with open("./data/anagrams.json") as file:
            self._data = json.load(file)
        return self._data


    ## Set/get the list of multiple word lists of this character length 
    def set_list_of_word_lists(self):
        word_len_str = str(self.word_length) 
        self._data = self.get_json_data()
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
    def set_word_list(self):
        if(self._list_of_word_lists):
            ## Get a random list out of the Parent list of word lists
            self._word_list = random.choice(self._list_of_word_lists)
            if(self._word_list):
                self.remove_word_list()
                return self._word_list
            else:
                print("!!!! Word_list is empty or not found.")
        else:
            print("!!!! Parent list of word lists is empty or not found.")
        return self._word_list
    

    ## Set/get 1 random word out of the 1 word list of this character length
    def set_anagram_word(self):
        if(self._word_list):
            self._anagram_word = random.choice(self._word_list)
            if(self._anagram_word):
                self.remove_word(self._anagram_word)
                return self._anagram_word
            else:
                print("!!!! Anagram_word is empty or not found.")    
        else:
            print("!!!! Word_list is empty or not found.")
        return self._anagram_word


    ## Remove this word list form the List of word lists of this character length
    def remove_word_list(self):
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
    def remove_word(self, word_to_remove):
        if(word_to_remove in self._word_list):
            self._word_list.remove(word_to_remove)
        else:
            print(word_to_remove, "NOT FOUND in Word List:", self._word_list)
        return
    

    def check_for_correct_answer(self, guess):
        guess = guess.lower()
        if(guess == self._anagram_word): ## Guessed same word as in the question
            print("\n* You can't guess: " + self._anagram_word.title() 
                  + ".  It's the same word as the question.  Please, try again.\n")
            self._is_correct_answer = False
        elif(guess in self._correct_guesses_list): ## Guessed same answer as guessed already 
            print("\n* You've guessed: " + guess.title() + " already.\n")
            self._is_correct_answer = False
        elif(guess in self._word_list): ## Guessed correctly
            print("\n*", guess.title(), "is correct!\n")
            self.remove_word(guess)
            self.increment_score()
            self._is_correct_answer = True
            self._correct_guesses_list.append(guess)    
        else: ## Guessed wrong
            print("\n* " + guess.title() + " is not a valid anagram of: " + self._anagram_word.upper() 
                  + ".  Please, try again.\n")
            self._is_correct_answer = False
        return self._is_correct_answer
    

    def increment_score(self):
        self._user_score += 1
        return self._user_score
    

    def display_user_score(self):
        print("Your score:", self._user_score)
        return


    def display_num_anagrams_left(self):
        if(self._timer.seconds > 0):
            if(len(self._word_list) > 0):
                print("* There are", len(self._word_list), "anagrams left to guess.")
            else:
                print("* You got all the anagrams for " + self._anagram_word.upper() + ".")
        return


    def display_correct_guesses(self):
        if(self._timer.seconds > 0 and len(self._correct_guesses_list) > 0):
            print("You've guessed correctly:", self._correct_guesses_list, "\n")
        return


    def display_time_left(self):
        if(self._timer.seconds > 0):
            print("* You have", self._timer.seconds, "seconds left.\n")
        elif(self._timer.seconds == 0):
            print(self._sorry_msg)
            self.quit_game()
        return


    def ask_question(self, word_to_anagram):
        word_to_anagram = word_to_anagram.upper()
        print("The word is:", word_to_anagram)
        print("There are " + str(len(self._word_list)) + " anagrams remaining for: " + word_to_anagram + ".")
        guess = input("Enter a guess: [q to quit] ")
        return guess
    
    
    def quit_game(self):
        self._timer.stop_timer()
        self._timer = None
        self._word_list = []
        self._list_of_word_lists = []
        self._user_score = 0
        self._user_answer = ""
        self._correct_guesses_list = []
        self._is_correct_answer = False
        print("Thanks for playing! TTFN!")
        return
    

    def play_game(self):
        while (len(self._list_of_word_lists) > 0 and self._timer.seconds > 0):
            while (len(self._word_list) > 0 and self._timer.seconds > 0):
                self._user_answer = self.ask_question(self._anagram_word)
                if (self._user_answer.lower() in ["q", "quit"]):
                    self.quit_game()
                    return
                is_correct = self.check_for_correct_answer(self._user_answer)
                self.display_user_score()
                self.display_correct_guesses()
                self.display_num_anagrams_left()
                self.display_time_left()
                while (not is_correct):
                    self._user_answer = self.ask_question(self._anagram_word)
                    if (self._user_answer.lower() in ["q", "quit"]):
                        self.quit_game()
                        return
                    is_correct = self.check_for_correct_answer(self._user_answer)
                    self.display_user_score()
                    self.display_correct_guesses()
                    self.display_num_anagrams_left()
                    self.display_time_left()
            else: ## Get the next word_list form the lists of lists of this char length:
                if(self._timer.seconds > 0):
                    self.set_word_list()
                    self.set_anagram_word()
                    self._correct_guesses_list = []
                else:
                    self.quit_game()
        else: ## There're no word lists left of this character length.
            self.quit_game()
        return
    

    def start_game(self):
        self.set_list_of_word_lists()
        self.set_word_list()
        self.set_anagram_word()
        print("* You have 60 seconds.\n")
        self._timer.start_timer()
        self.play_game()
        return
## END class

