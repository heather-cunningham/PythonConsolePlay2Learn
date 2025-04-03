from abc import ABCMeta, abstractmethod
from datetime import datetime, timezone
import time

## BEGIN
class Gameboard(metaclass=ABCMeta):
    """ Parent abstract class for the gameboards. """


    def __init__(self, game_name="", game_time=60):
        """ Creates an abstract parent Gameboard """
        super().__init__()
        ## Protected
        self._game_id = Gameboard._generate_game_id(game_name)
        self._game_date = Gameboard._set_game_date()
        self._game_name = game_name
        self._game_time = game_time
        self._final_score = 0
        self._is_game_ended = False
        self._was_game_quit = False
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def game_id(self):
        return self._game_id


    @property
    def game_date(self):
        return self._game_date


    @property
    def game_name(self):
        return self._game_name
    

    @game_name.setter
    def game_name(self, game_name=""):
        self._game_name = game_name
        return
    

    @property
    def game_time(self):
        return self._game_time
    

    @game_time.setter
    def game_time(self, game_time=60):
        self._game_time = game_time
        return
    

    @property
    def final_score(self):
        return self._final_score
    

    @final_score.setter
    def final_score(self, user_score=0):
        self._final_score = user_score
        return
    
    
    @property
    def was_game_quit(self):
        return self._was_game_quit
    

    @was_game_quit.setter
    def was_game_quit(self, was_game_quit):
        self._was_game_quit = was_game_quit        
        return
    

    @property
    def is_game_ended(self):
        return self._is_game_ended
    

    @is_game_ended.setter
    def is_game_ended(self, is_game_ended):
        self._is_game_ended = is_game_ended        
        return
    

    ## Protected
    @classmethod
    def _generate_game_id(cls, game_name):
        """ Generates a unique ID for this game played of the game's initials appended with
          '_' and the epoch. """
        if(game_name):
            game_name_arr = game_name.split(" ")
            id_num = int(time.time())
            id_for_game = ""
            if(len(game_name_arr) >= 2):
                for i in range(len(game_name_arr)):
                    id_for_game += game_name_arr[i][0:1].upper()
                id_for_game += "_" + str(id_num)
                return id_for_game
            else:
                id_for_game = game_name_arr[0][0:1].upper() + "_" + str(id_num)
                return id_for_game
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
    def _play_round(self):
        """ Runs game play or game mechanics. """
        pass


    @abstractmethod
    def _ask_question(self, parameter):
        """ Asks the game's question for the user to answer. """
        pass


    @abstractmethod
    def _check_for_correct_answer(self, answer):
        """ Checks if the user's answer is correct. """ 
        pass


    @abstractmethod    
    def _show_user_display(self):
        """ Show user info for the question just asked or answered, 
        (e.g.: current score, time left, correct answers so far, etc.). """
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
    def quit_gameboard(self):
        """ Allows the user to quit the game before it's completed. """
        pass


    @abstractmethod
    def _end_game(self):
        """ Ends the game. """
        pass
## END class
