from user import User
from helpers.margin_separator_module import get_margin_separator


GOODBYE_MSG = "Thanks for playing! TTFN (ta ta for now)!"


def prompt_player_for_user_info():
        prompt = ""
        while(prompt != "r" and prompt != "n"): 
            prompt = (
                input("Hiya! Are you a new or returning user? [n = new / r = returning]: ")
            ).strip().lower()
            if(prompt == "r"): ## returning User
                username = (input("Please, enter your username: ")).strip().replace(" ", "")
                if(User._check_username_exists(username)):
                    user = User.get_user_by_username(username)
                    if(user):
                        if(User._check_user_exists(user.user_id, username)):
                            print("Hi! ", user._full_name, ", welcome back!")
                            user_is_correct = ""
                            while(user_is_correct != "y" and user_is_correct != "n"):
                                user_is_correct = (
                                    input("Not you? [y = Yes, it's me / n = No, not me.] ")
                                ).strip().lower()
                                if(user_is_correct == "y"):
                                    user.is_new_user = False
                                    return user
                                else:
                                    prompt = "n"
                else:
                    print("Looks like you're a new user.\nUsername, " + username + ", could not be found.")
                    prompt = "n"
            elif(prompt == "n"): ## new User
                print("Welcome new user!  It's nice to see you here.")
                return None
            else:
                print("Invalid response: Please, enter either 'n' for new or 'r' for a returning user.")
        return None


def prompt_player_for_new_user_info():
    __MARGIN_STR = get_margin_separator()
    first_name = input("Please, enter your first name: ").strip().replace(" ", "").title()
    while(not User._validate_persons_name(first_name)):
        first_name = input("Please, enter your first name: ").strip().replace(" ", "").title()
    last_name = input("Please, enter your last name: ").strip().replace(" ", "").title()
    while(not User._validate_persons_name(last_name)):
        last_name = input("Please, enter your last name: ").strip().replace(" ", "").title()
    print("Please, create a username. Usernames must have or be:")    
    print(__MARGIN_STR)
    print("* Between 3 to 25 characters or less")
    print("* Alpha-numeric, underscore, and hyphen (dash) characters only")
    print("* No spaces")
    print("* Case sensitive")
    print("* Unique")
    new_username = (input("Please, enter a username: ")).strip().replace(" ", "")
    while(not User._validate_username(new_username)):
        new_username = (input("Please, enter a username: ")).strip().replace(" ", "")
    return (first_name, last_name, new_username)