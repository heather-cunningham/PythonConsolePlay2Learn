import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from helpers.margin_separator_module import get_margin_separator
from anagram_game.anagram_gameboard import AnagramGameboard
from helpers.player import Player


## BEGIN
class AnagramHunt():
    """ The Anagram Hunt game """

    
    def __init__(self):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()
        self._MARGIN_STR = get_margin_separator()
        self._GAME_TIME = 60
        self._word_length = 5
        self.is_game_over = False
        ## Python convention of explicitly returning, even if empty, to mark the end of a method.
        return


    @property
    def is_game_over(self):
        return self._is_game_over
    

    @is_game_over.setter
    def is_game_over(self, is_game_over):
        self._is_game_over = is_game_over
        return
    

    def welcome_player(self):
        print(self._MARGIN_STR)
        print("Welcome to Anagram Hunt!")
        print(self._MARGIN_STR)
        print("How many anagrams can you find in 60 seconds?")
        print(self._MARGIN_STR)
        return


    def select_word_length(self):
        self._word_length = 0
        ERROR_MSG = "is not a number from 5 through 8."
        while(self._word_length < 5 or self._word_length > 8):
            try:
                self._word_length = int(
                    input("To start, please select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print(f"{self._MARGIN_STR}\n{self._word_length} {ERROR_MSG}\n{self._MARGIN_STR}")
            else:
                if(self._word_length < 5 or self._word_length > 8):
                    print(f"{self._MARGIN_STR}\n{self._word_length} {ERROR_MSG}\n{self._MARGIN_STR}")
        return self._word_length
    

    def introduce_game(self, word_length=5):
        self._word_length = word_length
        print(self._MARGIN_STR)
        print("\n* You selected a word length of:", self._word_length, "characters.")
        print("* You have", self._GAME_TIME, 
              "SECONDS on the clock to enter as many anagrams as you can from a list of",
              self._word_length, "letter words, displayed one at a time.")
        print("* Answers MUST include all of the letters in the original word", 
              "to be considered a correct anagram.")
        print("* You MUST guess all of the correct anagrams for a displayed word", 
              "before progressing to the next in the list.")
        print("* Type a guess and press ENTER to submit an answer.")
        print("* Type 'zzz' at the prompt and press ENTER to quit.\n")
        return


    def create_gameboard(self, word_length=5):
        self._word_length = word_length
        gameboard = AnagramGameboard(self._word_length)
        return gameboard
    

    def check_player_ready(self):
        player_answer = (input("Are you ready to start playing Anagram Hunt? [y/n] ")).lower()
        return player_answer
    

    def ask_play_again(self):
        user_answer = (input("Want to play again? Press ENTER: [n/no to quit] ")).lower()
        return user_answer
## END class


## To run `anagram_hunt.py` stand-alone/individually
def main():
    game = AnagramHunt()
    ## While the game is not over:
    while(not game.is_game_over):
        player = Player()
        game.welcome_player()
        word_length = game.select_word_length()
        game.introduce_game(word_length)
        gameboard = game.create_gameboard(word_length)
        player_answer = game.check_player_ready()
        if(player_answer == "y" or player_answer == "yes"):
            player.is_player_ready = True
            gameboard.start_game()
            ## If the game is over, but wasn't quit:
            if(gameboard.is_game_ended and not gameboard.was_game_quit):
                user_answer = game.ask_play_again()
                if(user_answer == ""):
                    continue
                else:
                    gameboard.quit_game()
                    gameboard.was_game_quit = True
                    game.is_game_over = True
            else:
                game.is_game_over = True
                player_answer == "n"
                break
        else:
            player.is_player_ready = False
            gameboard.quit_game()
            game.is_game_over = True
    else:    
        del gameboard
        del game
    return


if(__name__ == "__main__"):
    main()