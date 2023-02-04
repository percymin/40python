import imaplib
import email
from email import policy 
import requests
import json

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

def find_encoding_info(txt):    
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'sammymin'
pw = 'awds4818~'
imap.login(id, pw)

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
	#받은 메일의 보낸사람 받은시간 제목을 문자열 형태로 바꿔준다.
    subject_str = str(subject)
    if subject_str.find("WEBSTORE") >= 0: # 메일의 "비밀번호" 라는 키워드가 있으면 찾은 위치를 반환한다. 못찾으면 -1을 반환한다.
        slack_send_message =  email_from + '\n' + email_date + '\n' + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)
		#"비밀번호" 키워드를 찾았으면 메일을 보내고 메일을 출력한다

imap.close()
imap.logout()