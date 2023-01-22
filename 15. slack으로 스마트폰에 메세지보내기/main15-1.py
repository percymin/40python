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
		if res.status_code == 200:
			return "ok"
		else:
			return "error"

print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메세지 입니다"))