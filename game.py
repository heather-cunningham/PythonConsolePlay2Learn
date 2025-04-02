from abc import ABCMeta, abstractmethod


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
    def _check_player_ready(self):
        pass


    @abstractmethod
    def _ask_play_again(self):
        pass


    @abstractmethod
    def _play_game(self, player=None):
        pass
## END class
