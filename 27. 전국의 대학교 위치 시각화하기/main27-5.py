import pandas as pd
import folium

filePath = r'27. 전국의 대학교 위치 시각화하기\학교주소좌표.xlsx'
#판다스를 이용하여 엑셀파일을 읽어온다
df_from_excel = pd.read_excel(filePath,engine='openpyxl',header=None)
#columns를 지정해준다
df_from_excel.columns = ['학교이름','주소','x','y']
#학교이름 주소 x y 를 리스트형태로 가져온다
name_list = df_from_excel['학교이름'].to_list()
addr_list = df_from_excel['주소'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

#기본 지도를 설정한다
map = folium.Map(location=[37,127],zoom_start=7)

#학교 이름의 갯수만큼 반복한다
for i in range(len(name_list)):
    #x 가 0이 아닐때 참이된다
    if position_x_list[i] != 0:
        #위도와 경도 값을 넣는다
        marker = folium.Marker([position_y_list[i],position_x_list[i]],
                            #이름을 넣는다
                            popup=name_list[i], 
                            icon = folium.Icon(color='blue'))
        marker.add_to(map) 

#저장ㅌ``
map.save(r'27. 전국의 대학교 위치 시각화하기/uni_map.html')