import time

## BEGIN
class User():
    """ A player or site user. """


    _registry_dict = {}


    def __init__(self, username=""):
        """ Creates a user with a unique id. """
        self._user_id = self.__generate_user_id()
        self._username = username
        ## Key: game_id, Value: List [ game_name, final_score ]
        self._all_games_played_dict = {}
        self.high_score = 0
        self.__check_user_exists_if_not_add(self)
        return
    

    @property
    def user_id(self):
        return self._user_id
    

    @property
    def username(self):
        return self._username


    def __generate_user_id(self):
        return int(time.time())
    

    def __add_user_to_registry(self, user_id):
        User._registry_dict[user_id] = self
        return


    def __check_user_exists_if_not_add(self):
        if(self.__class__.get_user_by_id(self._user_id) is None):
            self.__add_user_to_registry(self._user_id)
        else:
            raise ValueError("User with this user_id exists already.")
        return
    

    @classmethod
    def get_user_by_id(cls, user_id):
        """ Get this user from the dictionary by user_id. If not found, return None by default. 

        parameters: `user_id` (int) """
        return User._registry_dict.get(user_id, None)
    

    @classmethod
    def get_all_users(cls):
        """ Get all registered users returned in a dictionary with keys of user_ids
          and values of user properties. """
        return User._registry_dict

## END class
