## Play2Learn3
## Main module to serve as the entry point for Python Terminal version Play2Learn3 project


## BEGIN module
def main():
    """ A friendly, text-based 'homepage'. """
    margin_str = "-" * 65 
    print(margin_str)
    print("Welcome to Play2Learn3!")
    print(margin_str)
    print("A Python text-based console/terminal game program.")
    print(margin_str)
    print("Play2Learn3 contains 2 games:")
    print(margin_str)
    print("1.)  Anagram Hunt -- How many anagrams can you find in 60 seconds?")
    print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?\n")
    #
    game_to_play = 0
    err_msg = f"{margin_str}\nPlease, press 1 or 2 to select a game.\n{margin_str}"
    while(game_to_play != 1 and game_to_play != 2):
        try:
            game_to_play = int(input("Which game would you like to play? (1-Anagram Hunt / 2-Math Facts) "))
        except ValueError:
            print(err_msg)
        else:
            if(game_to_play != 1 and game_to_play != 2):
                print(err_msg)
            else:
                if(game_to_play == 1):
                    print("* You selected: 1.)  Anagram Hunt")
                else:
                    print("* You selected: 2.)  Math Facts")
## END module

if(__name__ == "__main__"):
    main()