import pandas as pd
import sqlite3

db_path=r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

#btc에서 중복된 값을 제외하고 불러온다
readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col = 'index')

#btc new라는 이름으로 새로 저장
readed_df.to_sql('BTC_NEW', con, if_exists='replace')

print(readed_df)

