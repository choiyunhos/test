import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from tqdm import trange
import re
import os

case_list = pd.read_csv('교통사고.csv')
contents = ['판시사항', '판결요지', '참조조문', '참조판례', '판례내용']

def remove_tag(content):
    cleaned_text = re.sub('<.*?>', '', content)
    return cleaned_text

for content in contents:
    case_list[content] = None

for i in trange(len(case_list)):
    url = "https://www.law.go.kr"
    link = case_list.loc[i]['판례상세링크'].replace('HTML', 'XML')
    url += link
    response = urlopen(url).read()
    xtree = ET.fromstring(response)

    for content in contents:
        text = xtree.find(content).text
        # 내용이 존재하지 않는 경우 None 타입이 반환되기 때문에 이를 처리해줌
        if text is None:
            text = '내용없음'
        else:
            text = remove_tag(text)
        case_list.at[i, content] = text
        
case_list.to_csv('교통사고_with_contents.csv', index=False)