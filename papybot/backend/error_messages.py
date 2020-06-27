import papybot.backend.constants as c
import random

# function to get random funny sentences when something goes wrong

def get_random_empty_message():
    """ gives random message when the user input is empty"""
    msg_answer = random.choice(c.FUNNY_SENTENCES)
    return msg_answer
    

def get_failed_msg():
    """ gives random messages when the spelling is wrong and nothing is found in
        Google and wikipedia"""
    msg_answer = random.choice(c.FAILED_MSG)

def get_no_history_msg():
    """ gives random messages when the something is wrong or nothing is found in
        wikipedia"""
    msg_answer = random.choice(c.NO_HISTORY_MSG)