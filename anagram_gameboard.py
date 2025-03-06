## BEGIN
class AnagramGameboard():
    """ The gameboard for Anagram Hunt. """
    margin_str = "-" * 65


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
        print("* You selected a word length of:", self.word_length, "characters.")
        print("* You have 60 seconds on the clock to enter as many anagrams you can think of from a list of",
              self.word_length, "letter words." )
        print("* Answers MUST include all of the letters in the original word to be considered a correct anagram.")


    
## END class
