import time

## BEGIN
class User():
    """ A player or site user. """


    __registry_dict = {}


    def __init__(self, user_id=None, username=""):
        """ Creates a user with a unique id or gets an existing user by `user_id`. 
        
        If `user_id` exists, the user is initialized from the registry, 
        else a new user is created. """
        if(user_id and self.__class__._check_user_exists(user_id)):
            ## If the user exists already, get the user by id:
            existing_user = self.__class__.get_user_by_id(user_id)
            if(existing_user):
                self.__initialize_existing_user(existing_user)
        else:
            self.__user_id = self.__generate_user_id()
            self.__username = username
            self.__is_new_user = True
            self.__all_games_played_dict = {}
            self.__high_score = 0
            self.__class__._add_user_to_registry(self)
        ## Former college Prof. convention of explicitly returning, even if empty, to mark the end of a method.
        return
    

    @property
    def user_id(self):
        return self.__user_id
    

    @property
    def username(self):
        return self.__username
    

    @username.setter
    def username(self, username):
        self.__username = username
        return
    

    @property
    def is_new_user(self):
        return self.__is_new_user
    

    @property
    def all_games_played_dict(self):
        return self.__all_games_played_dict
    

    @property
    def high_score(self):
        return self.__high_score
    

    @high_score.setter
    def high_score(self, high_score):
        self.__high_score = high_score
        return 


    ## Private
    def __initialize_existing_user(self, existing_user):
        """ Initialize an existing user from existing data. """
        self.__user_id = existing_user.user_id
        self.__username = existing_user.username
        self.__is_new_user = False
        self.__all_games_played_dict = existing_user.all_games_played_dict
        self.__high_score = existing_user.high_score
        

    ## Private
    def __generate_user_id(self):
        """ Generates a unique user_id from the epoch. """
        time.sleep(0.001)  # Small delay to avoid collisions
        user_id = int(time.time())
        if(not self.__class__._check_user_exists(user_id)):
            return user_id
        return None


    @classmethod
    def _check_user_exists(cls, user_id):
        return False if(cls.get_user_by_id(user_id) is None) else True 


    @classmethod
    def _add_user_to_registry(cls, user):
        """ Double check the user doesn't exist already, and if not add them to the registry.
        Else, do nothing. 
        
        parameters: `user` (object) """
        if(not cls._check_user_exists(user.user_id)):
            cls.__registry_dict[user.user_id] = user
        return
    

    @classmethod
    def get_user_by_id(cls, user_id):
        """ Get this user from the dictionary by user_id. If not found, return None by default. 

        parameters: `user_id` (int) """
        return cls.__registry_dict.get(user_id, None)
    

    @classmethod
    def get_all_users(cls):
        """ Get all registered users returned in a dictionary with keys of user_ids
          and values of user properties. """
        return cls.__registry_dict
## END class
