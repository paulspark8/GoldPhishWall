import email
import mailbox
from lib_b_mail import get_mail_text



if __name__ == "__main__":
    mailbox = mailbox.mbox("resources\\ai\\phishing-2022")
    for mail in mailbox:
        print('==================')
        print(get_mail_text(mail))
        print('==================')
        # break