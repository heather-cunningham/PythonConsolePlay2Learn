import json
import random
from pprint import pprint
from helpers.margin_separator_module import get_margin_separator


## BEGIN
class AnagramGameboard():
    """ The gameboard for Anagram Hunt. """

    
    margin_str = get_margin_separator()
    player_ready = "n"
    data = None
    list_of_word_lists = []
    word_list = []
    anagram_word = ""
    user_answer = ""
    user_score = 0
    is_correct_answer = False
    correct_guesses_list = []


    def __init__(self, word_length=5):
        """ Creates a gameboard for the Anagram Hunt game and game play.
         
        Keyword arguments: `word_length` (int) -- The number of characters for the length of the words from which
                                                  to make anagrams.  Defaults to 5. 
        """
        super().__init__()
        self.word_length = word_length


    # @property
    # def word_length(self):
    #     return self._word_length


    # @word_length.setter
    # def word_length(self, word_length):
    #     self._word_length = word_length


    # def ask_if_ready(self):
    #     self.player_ready = input("Are you ready to start playing? y/n ")
    #     return self.player_ready


    def introduce_game(self):
        print(self.margin_str)
        print("\n* You selected a word length of:", self.word_length, "characters.")
        print("* You have 60 SECONDS on the clock to enter as many anagrams as you can from a list of",
              self.word_length, "letter words, displayed one at a time.")
        print("* Answers MUST include all of the letters in the original word", 
              "to be considered a correct anagram.")
        print("* You MUST guess all of the correct anagrams for a displayed word", 
              "before progressing to the next in the list.")
        print("* Type a guess and press ENTER to submit an answer.\n")
        # self.ask_if_ready()
    

    ## Set/get the list of multiple word lists of this character length 
    def set_list_of_word_lists(self):
        word_len_str = str(self.word_length) 
        with open("./data/anagrams.json") as file:
            self.data = json.load(file)
        if(self.data):
            if(word_len_str in self.data):
                self.list_of_word_lists = self.data[word_len_str]
                # pprint(self.list_of_word_lists)
                return self.list_of_word_lists
            else:
                print("!!!!", word_len_str, "chars word length not found in data.")
        else:
            print("!!!! Data is empty or NOT FOUND")
        return self.list_of_word_lists
    

    ## Remove this word list form the List of word lists of this character length
    def remove_word_list(self):
        if(self.word_list in self.list_of_word_lists):
            self.list_of_word_lists.remove(self.word_list)
        else:
            print("Word List NOT FOUND in List of Lists:")
            print("Word List:\n", "-" * 25)
            pprint(self.word_list)
            print("List of Lists:\n", "-" * 25)
            pprint(self.list_of_word_lists)


    ## Remove this word from the current word list
    def remove_word(self, word_to_remove):
        if(word_to_remove in self.word_list):
            self.word_list.remove(word_to_remove)
        else:
            print(word_to_remove, "NOT FOUND in Word List:", self.word_list)


    ## Set/get 1 random list out of the list of multiple word lists of this character length
    def set_word_list(self):
        if(self.list_of_word_lists):
            ## Get a random list out of the Parent list of word lists
            self.word_list = random.choice(self.list_of_word_lists)
            if(self.word_list):
                self.remove_word_list()
                return self.word_list
        else:
            print("!!!! Parent list of word lists is empty or not found.")
        return self.word_list
    

    ## Set/get 1 random word out of the 1 word list of this character length
    def set_anagram_word(self):
        if(self.word_list):
            self.anagram_word = random.choice(self.word_list)
            if(self.anagram_word):
                self.remove_word(self.anagram_word)
                return self.anagram_word
        else:
            print("!!!! Word list is empty or not found.")
        return self.anagram_word
    

    def check_for_correct_answer(self, guess):
        guess = guess.lower()
        if(guess == self.anagram_word):
            print("\n* You can't guess: " + self.anagram_word 
                  + ".  It's the same word as the question.  Please, try again.\n")
            self.is_correct_answer = False
            return self.is_correct_answer
        elif(guess in self.correct_guesses_list):
            print("\n* You've guessed: " + guess + " already.\n")
            self.display_correct_guesses()
            self.is_correct_answer = False
            return self.is_correct_answer
        elif(guess in self.word_list):
            print("\n*", guess.title(), "is correct!\n")
            print("There are", len(self.word_list), "anagrams left to guess.")
            self.is_correct_answer = True
            self.remove_word(guess)
            self.correct_guesses_list.append(guess)
            return self.is_correct_answer    
        else:
            print("\n* " + guess.title() + " is not a valid anagram of: " + self.anagram_word.upper() 
                  + ".  Please, try again.\n")
            self.is_correct_answer = False
        return self.is_correct_answer


    def display_correct_guesses(self):
        if(len(self.correct_guesses_list) > 0):
            print("\nYou've guessed correctly:", )
            print("-" * 25)
            pprint(self.correct_guesses_list)
            print()
        return


    def ask_question(self, word_to_anagram):
        print("The word is:", word_to_anagram.upper())
        print("There are", len(self.word_list), "anagrams left to guess.")
        guess = input("Enter a guess: ")
        return guess


    def start_game(self):
        # if(self.player_ready.lower() == "y"):
        #
        ## Get all the lists of this char length:
        self.set_list_of_word_lists()
        self.set_word_list()
        self.set_anagram_word()
        while(len(self.list_of_word_lists) > 0 ):
            while(len(self.word_list) > 0):
                user_answer = self.ask_question(self.anagram_word)
                is_correct = self.check_for_correct_answer(user_answer)
                while(not is_correct):
                    user_answer = self.ask_question(self.anagram_word)
                    is_correct = self.check_for_correct_answer(user_answer)
                self.display_correct_guesses()
            else:
                self.set_word_list()
                self.set_anagram_word()
                self.correct_guesses_list = []
        else:
            print("Game Over")
            return
        # else:
        #     return    


## END class
