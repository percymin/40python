from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# 보낸메세지를 기록하는 빈 리스트를 만든다
send_message_list = []

while True:
    try:
        #사이트에 접속하여 제목과 링크를 찾는다
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        driver.implicitly_wait(time_to_wait=10)
        titles = driver.find_elements(By.CSS_SELECTOR,'#revolution_main_table > tbody > tr:nth-child(7) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        urls = driver.find_elements(By.CSS_SELECTOR,'#revolution_main_table > tbody > tr:nth-child(7) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')
        
		#revolution_main_table > tbody > tr:nth-child(7) > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font

        message=""
        for i in range(len(titles)):
            if "오예스"in titles[i].text:
                message = titles[i].text +"\n"+urls[i].get_attribute('href')
                #메세지를 처음보내는 경우일때
                if message not in send_message_list:
                    print(message)
                    send_message_list.append(message)
                    token = '5863921919:AAEu0y9RotBmdf-klgmkZJ3OJk6OnGgit7o'
                    id = "5920401541"
                    #텔레그램 메세지 전송
                    bot = telegram.Bot(token)
                    bot.sendMessage(chat_id=id, text=message)
                    
        time.sleep(60.0*5)
                
    except KeyboardInterrupt:
        break

	