from anagram_game.anagram_hunt import AnagramHunt
from anagram_game.anagram_gameboard import AnagramGameboard
from helpers.margin_separator_module import get_margin_separator


## Play2Learn3
## Main module to serve as the entry point for Python Terminal version Play2Learn3 project

## BEGIN module
_margin_str = get_margin_separator()


def greet_user():     
    print(_margin_str)
    print("Welcome to Play2Learn3!")
    print(_margin_str)
    print("A Python text-based console/terminal game program.")
    print(_margin_str)
    print("Play2Learn3 contains 2 games:")
    print(_margin_str)
    print("1.)  Anagram Hunt -- How many anagrams can you find in 60 seconds?")
    print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?\n")
    ## Python convention of explicitly returning, even if empty, to mark the end of a method.
    return



## Allows the user to select a game to play.
## returns: `game_to_play` (int) -- 1 for Anagram Hunt or 2 for Math Facts
def select_game():
    game_to_play = 0
    err_msg = f"{_margin_str}\nPlease, press 1 or 2 to select a game.\n{_margin_str}"
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
                print("* Let's go!!!\n")            
    return game_to_play


def launch_game(game_to_play):
    if(game_to_play == 1): ## Anagram Hunt
        game = AnagramHunt()
        game.welcome_player()
        word_len_selected = game.select_word_length()
        gameboard = game.create_gameboard(word_len_selected)
        gameboard.introduce_game()
        gameboard.start_game()
    else:
        print("\nSorry, the Math Facts game is UNDER CONSTRUCTION\n")
    return


def main():
    """ A friendly, text-based 'homepage'. """
    greet_user()
    game_to_play = select_game()
    launch_game(game_to_play)
    return    
## END module


if(__name__ == "__main__"):
    main()