import pyupbit
import sqlite3

# 한국돈으로 비트코인 데이터를 불러온다
ticker = 'KRW-BTC'
# 1분봉 데이터를 불러온다
interval = 'minute1'
#2021년 12월 2일 11시 20분 이전 데이터를 불러온다
to='2021-12-02 11:20'
#200개를 불러온다
count = 200
#비트코인 현재시세를 불러온다 정보는 위에 표시한것들을 이용하여 받아오겠다.
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

# 저장경로를 지정해준다 coin.db에다가 저장한다
db_path=r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
#데이터베이스 생성
con= sqlite3.connect(db_path, isolation_level=None)
#BTC의 이름으로 데이터를 생성후 데이터베이스에 추가(append)
price_now.to_sql('BTC', con, if_exists='append')

con.close