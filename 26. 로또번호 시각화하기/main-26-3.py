import pandas as pd
from collections import Counter

file_path = r'26. 로또번호 시각화하기\lotto1.xlsx'
df_from_excel = pd.read_excel(file_path,engine='openpyxl')

df_from_excel = df_from_excel.drop(index=[0,1])

df_from_excel.columns = [
                        '년도', '회차','추첨일','1등당첨자수',
                        '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
                        '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
                        '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
                        '당첨번호4','당첨번호5','당첨번호6','보너스번호'
                        ]
# 6개의 번호를 숫자형 타입으로 읽어 num_list에 더해준다
num_list = list(df_from_excel['당첨번호1'].astype(int))
num_list += list(df_from_excel['당첨번호2'].astype(int))
num_list += list(df_from_excel['당첨번호3'].astype(int))
num_list += list(df_from_excel['당첨번호4'].astype(int))
num_list += list(df_from_excel['당첨번호5'].astype(int))
num_list += list(df_from_excel['당첨번호6'].astype(int))
#가장 많이나온 숫자 45개를 찾는다
count = Counter(num_list)
most_num = count.most_common(45)
#가장 많이나온 숫자를 출력
print(most_num)