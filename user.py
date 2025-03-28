import time
import re
from collections import namedtuple
from helpers.margin_separator_module import get_margin_separator

## BEGIN
class User():
    """ A player or site user. """


    __registry_dict = {}
    GameData = namedtuple("GameData", 
                          ["game_name", "game_date", "final_score", "user_id", "username"])
    HighestScoreGame = namedtuple("HighestScoreGame", ["game_name", "high_score"])


    def __init__(self, user_id=None, username="", first_name="", last_name=""):
        """ Creates a user with a unique id or gets an existing user by `user_id`. 
        
        If `user_id` exists, the user is initialized from the registry, 
        else a new user is created. """
        if(user_id and self.__class__._check_user_exists(user_id, username)):
            ## If the user exists already, get the user by id:
            existing_user = self.__class__.get_user_by_id(user_id)
            if(existing_user):
                self.__initialize_existing_user(existing_user)
        else:
            self._first_name = first_name
            self._last_name = last_name
            self.__full_name = self.first_name + " " +  self.last_name 
            self.__user_id = self.__generate_user_id(username)
            self._is_new_user = True
            self._username = username
            self._all_games_played_dict = {}
            self._high_score = self.calc_high_score()
            self.__class__._add_user_to_registry(self)
        self._MARGIN_STR = get_margin_separator()
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def first_name(self):
        return self._first_name
    

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
        return
    

    @property
    def last_name(self):
        return self._last_name
    

    @last_name.setter
    def first_name(self, last_name):
        self._last_name = last_name
        return
    

    @property
    def _full_name(self):
        return self.__full_name
    

    @property
    def user_id(self):
        return self.__user_id


    @property
    def username(self):
        return self._username
    

    @username.setter
    def username(self, username):
        self._username = username
        return
    

    @property
    def is_new_user(self):
        return self._is_new_user
    

    @is_new_user.setter
    def is_new_user(self, is_new):
        self._is_new_user = is_new
        return 
    

    @property
    def all_games_played_dict(self):
        return self._all_games_played_dict
    

    @all_games_played_dict.setter
    def all_games_played_dict(self, games_played_dict):
        self._all_games_played_dict = games_played_dict
        return


    @property
    def high_score(self):
        return self._high_score
    

    @high_score.setter
    def high_score(self, high_score_tple):
        self._high_score = high_score_tple
        return 


    ## Private
    def __initialize_existing_user(self, existing_user):
        """ Initialize an existing user from existing data. """
        self._first_name = existing_user.first_name
        self._last_name = existing_user.last_name
        self.__full_name = existing_user.first_name + " " + existing_user.last_name 
        self.__user_id = existing_user.user_id
        self._username = existing_user.username
        self._is_new_user = False
        self.all_games_played_dict = existing_user.all_games_played_dict
        self.high_score = self.calc_high_score()
        

    ## Private
    def __generate_user_id(self, username):
        """ Generates a unique user_id from the epoch. """
        time.sleep(0.001)  ## Small delay to avoid collisions
        user_id = int(time.time())
        if(not self.__class__._check_user_exists(user_id, username)):
            return user_id
        return None
    

    @classmethod
    def _check_user_exists(cls, user_id, username):
        user = cls.get_user_by_id(user_id) 
        if(user):
            if(user.username == username):
                return True
        return False
    

    @classmethod
    def _check_username_exists(cls, username):
        """ Check if any User has this username already in the registry. 

        returns: True when first match is found, else False. """
        return any(user.username == username for user in cls.__registry_dict.values())


    @classmethod
    def _add_user_to_registry(cls, user):
        """ Double check the user doesn't exist already, and if not add them to the registry.
        Else, do nothing. 
        
        parameters: `user` (object) """
        if(not cls._check_user_exists(user.user_id, user.username)):
            cls.__registry_dict[user.user_id] = user
        return
        

    @classmethod
    def get_user_by_id(cls, user_id):
        """ Get this user from the registry dictionary by user_id. If not found, return None by default. 

        parameters: `user_id` (int) """
        return cls.__registry_dict.get(user_id, None)
    

    @classmethod
    def get_user_by_username(cls, username):
        """ Get this user from the registry dictionary by username. If not found, return None by default. 

        parameters: `username` (str) """
        for user in cls.__registry_dict.values():
            if user.username == username:
                user_obj = cls.get_user_by_id(user.user_id)
                if(user_obj):
                    return user_obj
        return None


    @classmethod
    def get_all_users(cls):
        """ Get all registered users returned in a dictionary with keys of user_ids
          and values of user properties. """
        return cls.__registry_dict
    

    @classmethod
    def _validate_username(cls, username):
        pattern = r'^[\w\-]+$'
        if(cls._check_username_exists(username)):
            print("Sorry, that username is in use already.")
            return False
        elif(len(username) > 25):
            print("Sorry, usernames must be 25 characters or less.")
            return False
        elif(not re.match(pattern, username)):
            print("Sorry, usernames may contain alpha-numeric characters, underscores, and hyphens (dashes) only.")
            return False
        return True
    

    @classmethod
    def _validate_persons_name(cls, persons_name):
        pattern = r'^[a-zA-Z\-]+$'
        if(len(persons_name) > 25):
            print("Sorry, first and last names must be 25 characters or less.")
            return False
        elif(not re.match(pattern, persons_name)):
            print("Sorry, first and last names may contain alphabetical characters and hyphens or dashes only.")
            return False
        return True


    def get_played_game_by_id(self, game_id):
        """ Get a played game from the user's dictionary of all played games by game_id. 
        If not found, return None by default. 

        parameters: `game_id` (str) """
        return self._all_games_played_dict.get(game_id, None)


    def add_games_to_all_played_games_dict(self, games_played_in_round_dict):
        """ Add games played in round to User's history of all games played if the game_id is  not
        in their `_all_games_played_dict` yet. 

        parameters: `games_played_in_round_dict` (dict) """
        for game_id in games_played_in_round_dict:
            if(not self.get_played_game_by_id(game_id)):
                game_data = self.__class__.GameData(
                    game_name = games_played_in_round_dict[game_id].game_name,
                    game_date = games_played_in_round_dict[game_id].game_date,
                    final_score = games_played_in_round_dict[game_id].final_score,
                    user_id = self.user_id,
                    username = self.username
                )
                self._all_games_played_dict[game_id] = game_data
        return
    

    def get_all_games_played_by_user_id(self):
        """ If this user exists in the registry, return all the games they've played. """
        user = self.__class__.get_user_by_id(self.user_id)
        if(user):
            return user.all_games_played_dict
        else:
            print("User not found. Can't get all user's played games.")
            return None


    def calc_high_score(self):
        played_games_dict = self.get_all_games_played_by_user_id()
        if(played_games_dict):
            game_id_w_max_score = max(
                played_games_dict.keys(),
                key=lambda game_id: played_games_dict[game_id].final_score 
            )
            game_name_w_max_score = played_games_dict[game_id_w_max_score].game_name
            max_score = played_games_dict[game_id_w_max_score].final_score
            high_score_game_data = self.__class__.HighestScoreGame(
                game_name = game_name_w_max_score,
                high_score = max_score
            )
        else:
            high_score_game_data = self.__class__.HighestScoreGame(
                game_name = "No games played yet",
                high_score = 0
            )
        self.high_score = high_score_game_data
        return high_score_game_data
## END class
