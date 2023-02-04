import imaplib
import email
from email import policy 
import requests
import json
import time

slack_webhook_url = "https://hooks.slack.com/services/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"



def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

def find_encoding_info(txt):    #보내는 데이터를 저장할 리스트를 생성했다
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'sammymin'
pw = 'awds4818~'
imap.login(id, pw)

send_list = []

while True:
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-5:] 

        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default) 

            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)
            
            if subject_str.find("WEBSTORE") >= 0: #메일에서 "비밀번호를" 찾았으면 ok
                slack_send_message =  email_from + '\n' + email_date + '\n' + subject_str
                if slack_send_message not in send_list: #send_list에 없다면 메일을 보낸다. (여러번 메일을 보내는 현상을 피하기위해서 새로 찾은것만 넣는 코드)
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message)
					# slack에서 메세지 보내고 send_list에 보낸 메세지를 원소로 추가

        time.sleep(30)
		#30초 지연
    except KeyboardInterrupt:
        break
	#키보드에 조작이 발생하면 반복문 반복문

imap.close()
imap.logout()