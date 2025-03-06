class AnagramHunt:
    def __init__(self, word_length=0):
        self.word_length = word_length


    @property
    def word_length(self):
        return self._word_length


    @word_length.setter
    def word_length(self, word_length):
        self._word_length = word_length


    def welcome_user(self):
        print("-" * 65)
        print("Welcome to Anagram Hunt!")
        print("-" * 65)
        print("How many anagrams can you find in 60 seconds?")
        print("-" * 65)


    def select_word_length(self):
        while(self.word_length < 5 or self.word_length > 8):
            try:
                self.word_length = int(
                    input("To start, please, select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print("Please, press 5 - 8 to select a word length.")
            else:
                if(self.word_length < 5 or self.word_length > 8):
                    print("Please, press 5 - 8 to select a word length.")
                else:
                    print("-" * 65)
                    print("You selected a word length of:", self.word_length, "characters.")
## END class


def main():
    game = AnagramHunt()
    game.welcome_user()
    game.select_word_length()


if(__name__ == "__main__"):
    main()