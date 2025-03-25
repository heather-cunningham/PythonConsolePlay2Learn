from collections import namedtuple
from user import User


## BEGIN
class Player(User):
    """ A game player """
    

    GameRoundData = namedtuple("GameRoundData", ["game_name", "game_date", "final_score"])


    def __init__(self, is_player_ready=False):
        """ Creates a player for a game """
        super().__init__()
        self._is_player_ready = is_player_ready
        self._games_played_in_round_dict = {}
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def is_player_ready(self):
        """ Is the player ready to start a game

         setter: Sets `is_player_ready` (bool) - whether the player is ready to 
         start playing a game or not. Defaults to False. """
        return self._is_player_ready
    

    @is_player_ready.setter
    def is_player_ready(self, is_player_ready=False):
        self._is_player_ready = is_player_ready
        return


    @property
    def games_played_in_round_dict(self):
        """ Dictionary to track the games played in this round, 
            e.g.: a round of Anagram Hunt or a round of Math Facts.
            
            Key = game_id
            Values = namedtuple, `GameRoundData`, which consists of attributes:
            # "game_name", "game_date", and "final_score". """
        return dict(self._games_played_in_round_dict)


    def add_game_played_in_round(self, game_id="", game_name="", game_date=None, final_score=0):
        if(game_id and game_name):
            if(game_id not in self._games_played_in_round_dict):
                game_round_data = self.__class__.GameRoundData(
                    game_name=game_name,
                    game_date=game_date,
                    final_score=final_score
                )
                self._games_played_in_round_dict[game_id] = game_round_data
            else:
                print("Game_id in this player's round's dictionary of played games already.")
        else:
            raise ValueError("Invalid or no game_id or game_name passed in.")
        return
        # return self._games_played_in_round_dict
## END class
