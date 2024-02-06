import json
import mailbox
from lib_b_mail import get_mail_text



if __name__ == "__main__":
    mailbox = mailbox.mbox("resources\\ai\\phishing-2022")
    mail_list=[]
    for mail in mailbox:
        # print('|=================')
        # print(mail['message-id'], mail['X-FDA'])
        # print('"'+get_mail_text(mail)+'",')
        mail_list.append(get_mail_text(mail))
        # get_mail_text(mail)
        # break
    with open("resources\\ai\\head_and_body_p2022.json", "w", encoding='utf-8') as f:
        json.dump(mail_list, f)
    
    with open("resources\\ai\\head_and_body_p2022.json", "r", encoding='utf-8') as f:
        mail_list = json.load(f)
        print(mail_list[1])