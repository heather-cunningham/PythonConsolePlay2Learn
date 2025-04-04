from abc import ABCMeta, abstractmethod
from helpers.prompt_player import GOODBYE_MSG


## BEGIN
class Game(metaclass=ABCMeta):
    """ Parent abstract class for the games. """


    def __init__(self, player=None):
        """ Creates an abstract parent Game """
        super().__init__()
        self._player = player
    

    @abstractmethod
    def _welcome_player(self, player=None):
        pass


    @abstractmethod
    def _introduce_game(self, parameter):
        pass


    @abstractmethod
    def _create_gameboard(self, game_configs):
        pass


    @abstractmethod
    def _play_game(self, player=None):
        pass


    @abstractmethod
    def _go_back_to_main_menu(self):
        pass


    @classmethod
    def check_player_ready(cls, game_name):
        player_answer = (
            input(f"Are you ready to start playing {game_name}? [y/n] ")
        ).strip().lower()
        return player_answer


    @classmethod
    def ask_play_again(cls):
        user_answer = (input("Want to play again? Press ENTER: [n/no to quit] ")).strip().lower()
        return user_answer


    @classmethod    
    def quit_game(cls):
        print(GOODBYE_MSG)
        return
## END class
