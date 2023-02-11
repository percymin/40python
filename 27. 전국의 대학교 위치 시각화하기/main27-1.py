#엑셀 데이터를 읽기위하여 판다스 라이브러리를 임포트한다
import pandas as pd

#엑셀 파일을 불러온다
filePath = r'27. 전국의 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2022).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')
#5번쨰 위치의 데이터를 colums로 설정 데이터의 이름임
df_from_excel.columns = df_from_excel.loc[4].tolist()
#0~5번째 줄은 삭제한다 중요한 데이터가 아니고 설명 같은거임
df_from_excel = df_from_excel.drop(index=list(range(0,5)))
#데이터의 앞쪽만 추력
print(df_from_excel.head())
#학교명 데이터를 출력
print(df_from_excel['학교명'].values)
#학교의 주소를 출력
print(df_from_excel['주소'].values)