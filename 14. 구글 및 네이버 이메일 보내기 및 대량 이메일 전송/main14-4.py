import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email = "sammymin@naver.com"
send_pwd = "awds4818~"

recv_email = "sammymin@naver.com"

smtp_name = "smtp.naver.com" 
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] ="html로 보내는 메일 입니다."
msg['From'] = send_email 
msg['To'] = recv_email 

html_body = """
<html>
<head>
<style>
table {
	border-style: solid;
}
td {
	border-style: solid;
}
</style>
</head>

<body>
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #0000ff;">글자의 색상을 지정하거나</span></p>
<h1>크기를 조정할수 있습니다.</h1>
<p>표도 만들수 있습니다.</p>
<table style="height: 83px; border-style: solid;" width="241">
<tbody>
<tr>
<td style="width: 73px; border-style: solid;">1</td>
<td style="width: 73px; border-style: solid;">2</td>
<td style="width: 73px; border-style: solid;">3</td>
</tr>
<tr>
<td style="width: 73px; border-style: solid;">표를</td>
<td style="width: 73px; border-style: solid;">만들수&nbsp;</td>
<td style="width: 73px; border-style: solid;">있습니다.</td>
</tr>
<tr>
<td style="width: 73px; border-style: solid;">4</td>
<td style="width: 73px; border-style: solid;">5</td>
<td style="width: 73px; border-style: solid;">6</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
</body>
</html>
"""

msg.attach( MIMEText(html_body,'html') ) 

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()