# import telegram
# import asyncio


# async def main(): #실행시킬 함수명 임의지정
#     token = "5863921919:AAEu0y9RotBmdf-klgmkZJ3OJk6OnGgit7o" 
#     id="5920401541"
#     bot = telegram.Bot(token = token)
#     await bot.send_message(chat_id=id, text='보낼메세지')

# asyncio.run(main()) #봇 실행하는 코드

import telegram
import asyncio
async def main():
	token = "5863921919:AAEu0y9RotBmdf-klgmkZJ3OJk6OnGgit7o" 
	id="5920401541"
	bot=telegram.Bot(token)
	await bot.sendMessage(chat_id=id, text="123")

asyncio.run(main())