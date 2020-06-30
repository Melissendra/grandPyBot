import papybot.backend.constants as c
import random

# function to get random funny sentences when something goes wrong

def get_random_empty_message():
    """ gives random message when the user input is empty"""
    return random.choice(c.FUNNY_SENTENCES)
    
def get_failed_msg():
    """ gives random messages when the spelling is wrong and nothing is found in
        Google and wikipedia"""
    return random.choice(c.FAILED_MSG)
    