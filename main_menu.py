from player import Player
from anagram_game.anagram_hunt import AnagramHunt
from math_game.math_facts import MathFacts
from helpers.margin_separator_module import get_margin_separator
from helpers.prompt_player import prompt_player_for_user_info, prompt_player_for_new_user_info, GOODBYE_MSG


## Play2Learn3
## Main module to serve as the entry point for Python Terminal version Play2Learn3 project

## BEGIN
class MainMenu():
    """ A friendly, text-based, Singleton 'homepage' or Main Menu. """


    _instance = None ## Singleton


    def __init__(self):
        """ Creates a Singleton the text-based homepage or main menu """
        # super().__init__()
        if(MainMenu._instance is None):
            MainMenu._instance = self
            ## Private Constant
            self.__MARGIN_STR = get_margin_separator()
            return
        else:
            raise Exception("#### An instance of MainMenu exists already.")
    

    @staticmethod
    def get_main_menu_instance():
        return MainMenu._instance
    

    @classmethod
    def rtn_to_main_menu(self):
        main_menu_instance = self.get_main_menu_instance()
        self.greet_user(main_menu_instance)
        game_to_play = self.select_game(main_menu_instance)
        if(game_to_play):
            self.launch_game(main_menu_instance, game_to_play)
        else: ## User quit
            self.quit_site(main_menu_instance)
        return   
    

    def greet_user(self):     
        print(self.__MARGIN_STR)
        print("Welcome to Play2Learn3!")
        print(self.__MARGIN_STR)
        print("A Python text-based console/terminal game program.")
        print(self.__MARGIN_STR)
        print("Play2Learn3 contains 2 games:")
        print(self.__MARGIN_STR)
        print("1.)  Anagram Hunt -- How many anagrams can you find in 60 seconds?")
        print("2.)  Math Facts -- How many arithmetic problems can you solve in 30 seconds?")
        print("* Type 'zzz' to quit.\n")
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return


    def quit_site(self):
        print(GOODBYE_MSG)
        return 


    ## Allows the user to select a game to play.
    ## returns: `game_to_play` (int) -- 1 for Anagram Hunt or 2 for Math Facts
    def select_game(self):
        game_to_play = 0
        err_msg = f"{self.__MARGIN_STR}\nPlease, press 1 or 2 to select a game.\n{self.__MARGIN_STR}"
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


    def launch_game(self, game_to_play):
        user = prompt_player_for_user_info()
        if(user): ## If returning User:
            player = Player(user_id=user.user_id, username=user.username)
        else: ## new user
            (new_first_name, new_last_name, new_username) = prompt_player_for_new_user_info()
            player = Player(user_id=None, username=new_username, first_name=new_first_name,
                            last_name=new_last_name)
        #
        if(game_to_play == 1): ## Anagram Hunt
            ## Pass the getter for the MainMenu's instance to the game being instantiated with 
            ## dependency injection to avoid circular imports of classes. 
            ## (I.e.: MainMenu imports the games' classes, so the games cannot import MainMenu.)
            ## This structure allows the games' classes to return to the MainMenu 
            ## when a player enters the games via the MainMenu.  
            anagram_hunt_game = AnagramHunt(player=player, get_main_menu_instance=self.get_main_menu_instance)
            anagram_hunt_game._play_game(player=player)
        elif(game_to_play == 2): ## Math Facts 
            math_facts_game = MathFacts(player=player, get_main_menu_instance=self.get_main_menu_instance)
            math_facts_game._play_game(player=player)
        else:
            raise ValueError("Invalid input! Neither Anagram Hunt, Math Facts, nor Quit selected.")
        return
## END class


def main():
    main_menu = MainMenu()
    main_menu.greet_user()
    game_to_play = main_menu.select_game()
    if(game_to_play):
        main_menu.launch_game(game_to_play)
    else: ## User quit
        main_menu.quit_site()
    return    



if(__name__ == "__main__"):
    main()