# 파이업비트 sqlite 날짜시간 라이브러리를 불러온다
import pyupbit
import sqlite3
import datetime

# datetime 라이브러리를 이용하여 시작날짜와 종료날짜의 모든 날을 리스트형태로 변환
def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    #이부분 설명을 잘 이해를 못하겠음
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    #위에랑 같은원리인듯한데 
    end = end + datetime.timedelta(days=1)
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2021-11-30", "2021-12-01")

print(dates)

#날짜를 뒤집는다reversed 최신날짜부터 데이터를 수집
for day in reversed(dates):
    myDay = day + ' 00:00'
    print(myDay)
    #하루치 1분봉의 데이터를 요청 1440 = 24시간 * 60분
    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440
    #비트코인 현재시세를 불러온다 정보는 위에 표시한것들을 이용하여 받아오겠다.
    price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

    print(price_now)
    
	#데이터베이스에 데이터 기록
    db_path=r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
    
    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', con, if_exists='append')
    
    con.close

