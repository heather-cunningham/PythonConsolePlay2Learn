## BEGIN
class Player():
    """ A game player """


    def __init__(self, is_player_ready=False):
        """ Creates a player for a game """
        super().__init__()
        self._is_player_ready = is_player_ready
        self._games_played_list = []
        ## Python convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def _is_player_ready(self):
        """ Is the player ready to start a game

         setter: Sets `is_player_ready` (bool) - whether the player is ready to 
         start playing a game or not. Defaults to False. """
        return self.__is_player_ready
    

    @_is_player_ready.setter
    def _is_player_ready(self, is_player_ready=False):
        self.__is_player_ready = is_player_ready
        return

## END class
