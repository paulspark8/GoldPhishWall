import email
import re
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


def _convert_html_2_text(text: str) -> str:
    info = re.sub("<[^<>]+>",_uppercase_tags, text)
    print(info)
    if any(tag in info for tag in ['<html', '<body', '<head', '<div', '<p', '<table']):
        return info.strip()
    
    return _get_only_text(info).strip()

def _uppercase_tags(match):
    # print(match.group())
    return match.group().lower()
    
def _tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def _get_only_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(_tag_visible, texts)
    return u" ".join(print(t.strip()) for t in visible_texts)

def _get_text_from_image(image):
    return '++ Image ++ \n'

def _parse_mail_text(mail: email.message.Message) -> str:
    text = ''
    if not mail.is_multipart():
        text = _convert_html_2_text(mail.get_payload(decode=True).decode(errors='ignore'))
    for part in mail.walk():
        content_type = part.get_content_type()
        if content_type in ['text/html', 'text/plain']:
            text += _convert_html_2_text(part.get_payload(decode=True).decode(errors='ignore')+'\n')
            # break
        elif "image" in content_type:
            text+=_get_text_from_image(content_type)
        elif "multipart" not in content_type:
            text+=part.get_content_type()
    return text

def _get_decode_mail_subject(mail: email.message.Message) -> str:
    try:
        subj = mail["subject"].strip()
        if not subj.startswith("=?"):
            return subj
        else:
            return decode_header(subj)[0][0].decode().strip()
    except Exception:
        return "[WARNING] Subject error or no subject"

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
