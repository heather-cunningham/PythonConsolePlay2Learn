from margin_separator_module import get_margin_separator


## BEGIN
class AnagramGameboard():
    """ The gameboard for Anagram Hunt. """
    margin_str = get_margin_separator()


    def __init__(self, word_length=5):
        """ Creates a gameboard for the Anagram Hunt game and game play.
         
        Keyword arguments: `word_length` (int) -- The number of characters for the length of the words from which
                                                  to make anagrams.  Defaults to 5. 
        """
        super().__init__()
        self.word_length = word_length


    @property
    def word_length(self):
        return self._word_length


    @word_length.setter
    def word_length(self, word_length):
        self._word_length = word_length


    def introduce_game(self):
        print(self.margin_str)
        print("\n* You selected a word length of:", self.word_length, "characters.")
        print("* You have 60 SECONDS on the clock to enter as many anagrams as you can from a list of",
              self.word_length, "letter words, displayed one at a time.")
        print("* Answers MUST include all of the letters in the original word", 
              "to be considered a correct anagram.")
        print("* You MUST guess all of the correct anagrams for a displayed word", 
              "before progressing to the next in the list.\n")


    
## END class
