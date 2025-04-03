from player import Player
from anagram_game.anagram_hunt import AnagramHunt
from math_game.math_facts import MathFacts
from helpers.margin_separator_module import get_margin_separator
from helpers.prompt_player import prompt_player_for_user_info, prompt_player_for_new_user_info, GOODBYE_MSG


## Play2Learn3
## Main module to serve as the entry point for Python Terminal version Play2Learn3 project

## BEGIN module
_MARGIN_STR = get_margin_separator()


def greet_user():     
    print(_MARGIN_STR)
    print("Welcome to Play2Learn3!")
    print(_MARGIN_STR)
    print("A Python text-based console/terminal game program.")
    print(_MARGIN_STR)
    print("Play2Learn3 contains 2 games:")
    print(_MARGIN_STR)
    print("1.)  Anagram Hunt -- How many anagrams can you find in 60 seconds?")
    print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?")
    print("* Type 'zzz' to quit.\n")
    ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
    return


def quit():
    print(GOODBYE_MSG)
    return 


## Allows the user to select a game to play.
## returns: `game_to_play` (int) -- 1 for Anagram Hunt or 2 for Math Facts
def select_game():
    game_to_play = 0
    err_msg = f"{_MARGIN_STR}\nPlease, press 1 or 2 to select a game.\n{_MARGIN_STR}"
    while(game_to_play != 1 and game_to_play != 2):
        try:
            game_to_play = input(
                "Which game would you like to play? (1-Anagram Hunt / 2-Math Facts) ['zzz' to quit] "
            )
            if(game_to_play == "zzz"):
                return "" ## Return a falsy value to quit
            game_to_play = int(game_to_play)
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
    user = prompt_player_for_user_info()
    if(user): ## If returning User:
        player = Player(user_id=user.user_id, username=user.username)
    else: ## new user
        (new_first_name, new_last_name, new_username) = prompt_player_for_new_user_info()
        player = Player(user_id=None, username=new_username, first_name=new_first_name,
                        last_name=new_last_name)
    #
    if(game_to_play == 1): ## Anagram Hunt
        anagram_hunt_game = AnagramHunt()
        anagram_hunt_game._play_game(player=player)
    elif(game_to_play == 2): ## Math Facts 
        math_facts_game = MathFacts()
        math_facts_game._play_game(player=player)
    else:
        raise ValueError("Invalid input! Neither Anagram Hunt, Math Facts, nor Quit selected.")
    return


def main():
    """ A friendly, text-based 'homepage'. """
    greet_user()
    game_to_play = select_game()
    if(game_to_play):
        launch_game(game_to_play)
    else: ## User quit
        quit()
    return    
## END module


if(__name__ == "__main__"):
    main()