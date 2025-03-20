from player import Player
from anagram_game.anagram_hunt import AnagramHunt
from helpers.margin_separator_module import get_margin_separator


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
    print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?\n")
    ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
    return



## Allows the user to select a game to play.
## returns: `game_to_play` (int) -- 1 for Anagram Hunt or 2 for Math Facts
def select_game():
    game_to_play = 0
    err_msg = f"{_MARGIN_STR}\nPlease, press 1 or 2 to select a game.\n{_MARGIN_STR}"
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
        ## While the game is not over:
        while(not game._is_game_over):
            player = Player()
            game.welcome_player()
            word_length = game.select_word_length()
            game.introduce_game(word_length)
            gameboard = game.create_gameboard(word_length)
            player_answer = game.check_player_ready()
            if(player_answer == "y" or player_answer == "yes"):
                player._is_player_ready = True
                gameboard.start_game()
                ## If the game is over, but wasn't quit:
                if(gameboard._is_game_ended and not gameboard._was_game_quit):
                    player.add_game_played(gameboard._game_id, gameboard._GAME_NAME, gameboard._game_date, 
                                        gameboard._final_score)
                    user_answer = game.ask_play_again()
                    if(user_answer == ""):
                        continue
                    else:
                        gameboard.quit_game()
                        gameboard._was_game_quit = True
                        game._is_game_over = True
                else:
                    game._is_game_over = True
                    player_answer == "n"
                    break
            else:
                player._is_player_ready = False
                gameboard.quit_game()
                game._is_game_over = True
        else:    
            del gameboard
            del game
    elif(game_to_play == 2):
        print("\nSorry, the Math Facts game is UNDER CONSTRUCTION\n")
    else:
        print("Invalid input!  Please, select: 1 for Anagram Hunt or 2 for Math Facts.")
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