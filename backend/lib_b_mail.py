import email
from bs4 import BeautifulSoup
from bs4.element import Comment
from enum import Enum
from email.header import decode_header

import chardet


class Log_type(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    CRITICAL = 3
    DEAD = 4


def _get_text_from_image(image):
    t = '++ Image ++ \n'
    return ''


def _get_only_clean_text(dirty_text):
    soup = BeautifulSoup(dirty_text, 'html.parser')
    clean_text = soup.get_text(strip=True, separator=' ')
    return clean_text+'\n'


def _parse_mail_text(mail: email.message.Message) -> str:
    text = ''
    if not mail.is_multipart():
        t = mail.get_payload(decode=True).decode(errors='ignore')
        return _get_only_clean_text(t)
    for part in mail.walk():
        content_type = part.get_content_type()
        if content_type == 'text/plain':
            t = part.get_payload(decode=True).decode(
                errors='ignore').strip()+'\n'
            text += _get_only_clean_text(t)
        elif content_type == 'text/html':
            t = part.get_payload(decode=True).decode(
                errors='ignore').strip()+'\n'
            text += _get_only_clean_text(t)
        elif "image" in content_type:
            t = _get_text_from_image(content_type)
            text += _get_only_clean_text(t)
        elif "multipart" not in content_type:
            text += part.get_content_type()
    return text


def _get_decode_mail_subject(mail: email.message.Message) -> str:
    try:
        subj = mail["subject"].strip()
        if not subj.startswith("=?"):
            return subj
        else:
            return _get_only_clean_text(decode_header(subj)[0][0].decode().strip())
    except Exception:
        return "[W] Subject error or no subject"


def get_mail_text(mail: email.message.Message):
    # Get subject
    text = ''
    text = _get_decode_mail_subject(mail).replace("\n", " ") + "\n\n"
    text += _parse_mail_text(mail)

    return text


def create_log_entry(type: Log_type):
    pass


def delete_log_entry():
    pass


def send_log_entry():
    pass


def export_log_entry():
    pass


def print_log_entry():
    pass
