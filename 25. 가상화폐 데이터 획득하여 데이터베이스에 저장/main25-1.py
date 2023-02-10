#파이업비트 라이브러리 불러옴
import pyupbit

# 거래되고있는 가상화폐 한국말로 표시
coin_lists = pyupbit.get_tickers(fiat='KRW')
# 가상화폐 목록 출력
print(coin_lists)

#비트코인 이더리움 현재 시세 표시
price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
#현재 시세 출력
print(price_now)