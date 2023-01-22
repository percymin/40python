import telegram

token = '5863921919:AAEu0y9RotBmdf-klgmkZJ3OJk6OnGgit7o'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
	print(u.message)