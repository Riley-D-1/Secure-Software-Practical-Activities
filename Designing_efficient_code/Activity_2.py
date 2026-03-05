import time
import datetime
sessions = {}

def create_session(user_id):
    # Sets login_time to None - improve this to capture the actual login time (current timestamp)
    sessions[user_id] = {'data': {}, 'login_time': datetime.datetime.now()}

def login_user(user_id):
    sessions[user_id]['login_time'] = datetime.datetime.now() # This should be replaced with the real current time

def is_session_active(user_id,timeout):
    print("Filler")

# Task:
# - Update create_session and login_user to correctly store the current login timestamp.
# - Implement a function is_session_active(user_id, timeout) that returns True if the user session is active within the timeout period.


# Is incomplete as not sure of what I'm meant to do for the second step