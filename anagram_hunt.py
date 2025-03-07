from margin_separator_module import get_margin_separator
from anagram_gameboard import AnagramGameboard

## BEGIN
class AnagramHunt:
    """ The Anagram Hunt game """
    ## What does Anagram Hunt start page have?
    ## * itself
    margin_str = get_margin_separator()  

    
    def __init__(self):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()


    ## What can Anagram Hunt start page do?
    # * Welcome the user
    # * Ask user to choose a word length
    # * Create the gameboard -- How does it do this?
    #### ** Instantiate the gameboard


    def welcome_player(self):
        print(self.margin_str)
        print("Welcome to Anagram Hunt!")
        print(self.margin_str)
        print("How many anagrams can you find in 60 seconds?")
        print(self.margin_str)


    def select_word_length(self):
        word_length = 0
        error_msg = "is not a number from 5 through 8."
        while(word_length < 5 or word_length > 8):
            try:
                word_length = int(
                    input("To start, please select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print(f"{self.margin_str}\n{word_length} {error_msg}\n{self.margin_str}")
            else:
                if(word_length < 5 or word_length > 8):
                    print(f"{self.margin_str}\n{word_length} {error_msg}\n{self.margin_str}")
        return word_length


    def create_gameboard(self, word_length):
        gameboard = AnagramGameboard(word_length)
        return gameboard
## END class

""" To run `anagram_hunt.py` stand-alone/individually """
def main():
    game = AnagramHunt()
    game.welcome_player()
    word_length = game.select_word_length()
    gameboard = game.create_gameboard(word_length)
    gameboard.introduce_game()


if(__name__ == "__main__"):
    main()