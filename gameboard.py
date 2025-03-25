from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone
import time

## BEGIN
class Gameboard(metaclass=ABCMeta):
    """ Parent abstract class for the games. """


    def __init__(self, game_name=""):
        """ Creates an abstract parent Game """
        super().__init__()
        ## Public
        self.game_name = game_name
        ## Protected
        self._final_score = 0
        self._game_id = Gameboard._generate_game_id(game_name)
        self._game_date = Gameboard._set_game_date()
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def game_name(self):
        return self._game_name
    

    @game_name.setter
    def game_name(self, game_name=""):
        self._game_name = game_name
        return
    
    @property
    def final_score(self):
        return self._final_score
    

    @final_score.setter
    def final_score(self, final_score=0):
        self._final_score = final_score
        return
    

    ## Protected
    @classmethod
    def _generate_game_id(cls, game_name):
        """ Generates a unique ID for this game played of the game's initials appended with
          '_' and the epoch. """
        if(game_name):
            game_name_arr = game_name.split(" ")
            id_num = int(time.time())
            id = ""
            if(len(game_name_arr) >= 2):
                for i in range(len(game_name_arr)):
                    id += game_name_arr[i][0:1].upper()
                id += "_" + str(id_num)
                return id
            else:
                id = game_name_arr[0][0:1].upper() + "_" + str(id_num)
                return id
        return None


    ## Protected
    @classmethod
    def _set_game_date(cls):
        """ Sets the UTC date and time of the day and time the game was played, 
        and returns it as a formatted string. """
        now = datetime.now(timezone.utc)
        return now.strftime("%Y-%m-%d %H:%M:%S UTC")


    @abstractmethod
    def start_game(self):
        """ Starts the game. """
        pass


    @abstractmethod
    def _start_game_timer(self):
        """ Starts the game timer. """
        pass


    @abstractmethod
    def _play_game(self):
        """ Runs game play or game mechanics. """
        pass


    @abstractmethod
    def _ask_question(self):
        """ Asks the game's question for the user to answer. """
        pass


    @abstractmethod
    def _check_for_correct_answer(self):
        """ Checks if the user's answer is correct. """ 
        pass


    @abstractmethod
    def _increment_score(self):
        """ Increases the user's score upon a correct answer. """
        pass


    @abstractmethod
    def _stop_game_timer(self):
        """ Stops the game timer. """
        pass


    @abstractmethod
    def _reset_game(self):
        """ Resets the game. """
        pass


    @abstractmethod
    def quit_game(self):
        """ Allows the user to quit the game before it's completed. """
        pass


    @abstractmethod
    def _end_game(self):
        """ Ends the game. """
        pass
## END class
