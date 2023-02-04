import imaplib
import email
from email import policy 

def find_encoding_info(txt):    
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode
# 문자열을 인코딩한다. ==사용자가 입력한 문자나 기호들을 컴퓨터가 이용할 수 있는 신호로 만드는 것을 말한다.

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'sammymin'
pw = 'awds4818~'
imap.login(id, pw)
#네이버 메일에 로그인한다.

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:] 
#받은 메일함에서(받은메일=inbox) 메일을 읽는다 last_email = all_email[-5:] 최신 5개의 이메일만 읽는다

for mail in reversed(last_email): #last main을 뒤집어(reversed) 출력한다
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)
	#메일을 읽는다 

    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)
    print('='*70)
	#읽은 메일의 정보를 출력한다(보낸사람 받)

imap.close()
imap.logout()