import email
from enum import Enum
class Logtype(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    CRITICAL = 3
    DEAD = 4

def get_mail_text():
    pass

def create_log_entry(type: Logtype):
    pass

def delete_log_entry():
    pass

def send_log_entry():
    pass

def export_log_entry():
    pass

def print_log_entry():
    pass

