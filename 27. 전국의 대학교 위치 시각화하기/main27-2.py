import requests

#api의 접속 내영
url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'   #도로명주소
road_type2 = 'PARCEL' #지번주소
address = '&address='
keys = '&key='
primary_key = '693598C2-0E00-3498-B514-EAD0B01C5CD5'

#주소를 x y 좌표로 변환해주는 함수 api에 접속하여 x y부분만 분리하여 반환합니다
def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x,y
    else:
        x = 0
        y = 0
        return x,y

# 한국산업기술대학교의 x y 값을 출력
x,y = request_geo("경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)")

print(f'x값: {x}')
print(f'y값: {y}')


