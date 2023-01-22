import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 

send_email = "sammymin@naver.com"
send_pwd = "awds4818~"

recv_email = "sammymin@naver.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] ="test222222"
msg['From'] = send_email 
msg['To'] = recv_email 

text = """
test2222222222222
"""
contentPart = MIMEText(text) 
msg.attach(contentPart) 

etc_file_path = r'14. 구글 및 네이버 이메일 보내기 및 대량 이메일 전송\첨부파일.txt'
with open(etc_file_path, 'rb') as f : 
    etc_part = MIMEApplication( f.read() )
    etc_part.add_header('Content-Disposition','attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()