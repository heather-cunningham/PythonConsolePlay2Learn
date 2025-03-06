## Play2Learn3
## Main module to serve as the entry point for Python Terminal version Play2Learn3 project


## Text-based UI "homepage"
def main():
    """ A friendly, text-based 'homepage'. """
    print("-" * 65)
    print("Welcome to Play2Learn3!")
    print("-" * 65)
    print("A Python text-based console/terminal game program.")
    print("-" * 65)
    print("Play2Learn3 contains 2 games:")
    print("-" * 65)
    print("1.)  Anagram Hunt -- How many anagrams can you find in 60 seconds?")
    print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?\n")
    game_to_play = "0"
    while(game_to_play != "1" and game_to_play != "2"):
        game_to_play = input("Which game would you like to play? (1-Anagram Hunt / 2-Math Facts) ")
        print("-" * 65)
        if(game_to_play != "1" and game_to_play != "2"):
            print("Please, press 1 or 2 to select a game.")
        else:
            if(game_to_play == "1"):
                print("You selected 1.)  Anagram Hunt")
            else:
                print("You selected 2.)  Math Facts")


if(__name__ == "__main__"):
    main()