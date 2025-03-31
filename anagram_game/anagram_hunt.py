import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from pprint import pprint
from helpers.margin_separator_module import get_margin_separator
from anagram_game.anagram_gameboard import AnagramGameboard


## BEGIN
class AnagramHunt():
    """ The Anagram Hunt game """

    
    __GAME_NAME = "Anagram Hunt"
    __GAME_TIME = 60
    

    def __init__(self, player=None):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()
        ## Private
        self.__MARGIN_STR = get_margin_separator()
        ## Protected
        self._player = player
        self._word_length = 5
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
        print("How many anagrams can you find in", self.__class__.__GAME_TIME, "seconds?")
        print(self.__MARGIN_STR)
        return


    ## Private
    def __select_word_length(self):
        self._word_length = 0
        ERROR_MSG = "is not a number from 5 through 8."
        while(self._word_length < 5 or self._word_length > 8):
            try:
                self._word_length = int(
                    input("To start, please select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print(f"{self.__MARGIN_STR}\n{self._word_length} {ERROR_MSG}\n{self.__MARGIN_STR}")
            else:
                if(self._word_length < 5 or self._word_length > 8):
                    print(f"{self.__MARGIN_STR}\n{self._word_length} {ERROR_MSG}\n{self.__MARGIN_STR}")
        return self._word_length
    

    def introduce_game(self, word_length=5):
        self._word_length = word_length
        print(self.__MARGIN_STR)
        print("\n* You selected a word length of:", self._word_length, "characters.")
        print("* You have", self.__class__.__GAME_TIME, 
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
        gameboard = AnagramGameboard(game_name=self.__class__.__GAME_NAME, game_time=self.__class__.__GAME_TIME, 
                                     word_length=self._word_length)
        return gameboard
    

    def check_player_ready(self):
        player_answer = (
            input(f"Are you ready to start playing {self.__class__.__GAME_NAME}? [y/n] ")
        ).strip().lower()
        return player_answer
    

    def play_anagram_hunt(self, player=None):
        ## While the game is not over:
        while(not self.is_game_over):
            self.welcome_player(player)
            word_length = self.__select_word_length()
            self.introduce_game(word_length)
            gameboard = self.create_gameboard(word_length)
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


## To run `anagram_hunt.py` stand-alone/individually
def main():
    game = AnagramHunt()
    game.play_anagram_hunt() 
    return


if(__name__ == "__main__"):
    main()