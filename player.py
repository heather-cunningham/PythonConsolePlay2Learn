## BEGIN
class Player():
    """ A game player """


    """ Dictionary to track the games played in this round, 
    e.g.: a round of Anagram Hunt or a round of Math Facts.
    
    Key = game_id
    Values = List of dicts: 
    [{"Game Name": game_name}, {"Game Date": game_date}, {"Final Score": final_score}] """
    _games_played_in_round_dict = {}


    def __init__(self, is_player_ready=False):
        """ Creates a player for a game """
        super().__init__()
        self._is_player_ready = is_player_ready
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
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


    def add_game_played_in_round(self, game_id="", game_name="", game_date=None, final_score=0):
        if(game_id not in self._games_played_in_round_dict):
            self._games_played_in_round_dict[game_id] = [{"Game Name": game_name}, {"Game Date": game_date}, 
                                               {"Final Score": final_score}]
        else:
            raise ValueError("Game_id in the player's played games in this round's dictionary already.")
        return self._games_played_in_round_dict


## END class
