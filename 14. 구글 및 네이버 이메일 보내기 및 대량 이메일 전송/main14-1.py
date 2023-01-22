import smtplib
from email.mime.text import MIMEText

send_email = "sammymin@naver.com"
send_pwd = "awds4818~"

recv_email = "sammymin@naver.com"

smtp_name = "smtp.naver.com" 
smtp_port = 587

text = """
메일 내용111111111111111
"""
msg = MIMEText(text)

msg['Subject'] ="메일제목1111111111"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()