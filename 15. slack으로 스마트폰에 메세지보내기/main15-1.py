import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"
#자신의 슬렉 웹훅 url을 입력한다


def sendSlackWebhook(strText):
	headers = {
		"Content-type": "application/json"
	}

	data = {
		"text" : strText
	}

	res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
	#json을 이용하여 webhook방식으로 메시지를 보내는 함수

	if res.status_code == 200:
		return "ok"
		#satus == 200일때 즉 성공할때는 ok를 출력하게 한다
	else:
		return "error"
		#status 200이 아닐때 즉 실패했을때는 error를 출력하게 한다.


print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메세지 입니다"))
#ok가 되면 "안녕하세요 파이썬에서 보내는 메세지 입니다"를 슬렉에서 보낸다.