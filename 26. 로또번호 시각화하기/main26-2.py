import pandas as pd
#그래프를 그리기위해 matplotlib 라이브러리를 불러온다
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

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

# 엑셀파일을 확인하면 당첨금액이 숫자+,+원으로 되어있는데 콤마와 원 을 지운다
df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
#값을 숫자형태로 다시 데이터프레임에 저장한다
df_from_excel["1등당첨금액"] = pd.to_numeric(df_from_excel["1등당첨금액"])
df_from_excel["2등당첨금액"] = pd.to_numeric(df_from_excel["2등당첨금액"])
df_from_excel["3등당첨금액"] = pd.to_numeric(df_from_excel["3등당첨금액"])
df_from_excel["4등당첨금액"] = pd.to_numeric(df_from_excel["4등당첨금액"])
df_from_excel["5등당첨금액"] = pd.to_numeric(df_from_excel["5등당첨금액"])

print( df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']] )

#그래프의 이름을 표시할때 한글을 이용하기위해 폰트를 설정
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

#회차의 마지막 100개의 데이터만 x축으로 이용한다
x = df_from_excel['회차'].iloc[:100].values
#당첨금액의 마지막 100개의 데이터만 y축으로 사용하고 단위는 억으로 하기위해 1억을 나눈다
price = df_from_excel['1등당첨금액'].iloc[:100].values / 100000000

#그래프의 초기 사이즈를 정한다
plt.figure(figsize=(10, 5))
#x축 라벨을 회차 라고 설정
plt.xlabel('회차') 
#y축 라벨을 당첨금액 이라고 설정
plt.ylabel('당첨금액(단위:억원)') 
#바의 x,y값과 폭을 지정하여 그래프를 그린다
plt.bar(x, price, width=0.4)
#그래프를 표시
plt.show()