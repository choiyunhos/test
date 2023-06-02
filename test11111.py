import requests
import xml.etree.ElementTree as ET

url = "http://www.dtro.or.kr/openApi/lostInfo.xml"

# 요청 보내고 응답 받기
response = requests.get(url)

# 응답이 성공적으로 도착했는지 확인
if response.status_code == 200:
    # XML 데이터 가져오기
    xml_data = response.text
    
    # XML 파싱
    root = ET.fromstring(xml_data)
    
    # 이후 데이터 처리를 위한 작업 수행
    # 예시: 모든 항목 출력
    for item in root.findall("item"):
        name = item.find("name").text
        age = item.find("age").text
        print(f"Name: {name}, Age: {age}")
else:
    print("요청이 실패했습니다.")
