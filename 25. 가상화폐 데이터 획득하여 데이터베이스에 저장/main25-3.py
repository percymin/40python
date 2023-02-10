#판다스 라이브러리를 불러온다
import pandas as pd
import sqlite3

#데이터베이스에 접속한다
db_path = r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con= sqlite3.connect(db_path, isolation_level=None)

#판다스를 이용하여 데이터베이스를 읽는다
readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col='index')
#읽은데이터를 출력
print(readed_df)
