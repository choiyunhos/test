import pandas as pd
from konlpy.tag import Okt
import re

# 데이터 불러오기
case_list = pd.read_csv('교통사고_with_contents.csv', encoding='cp949')


# 텍스트 데이터 정제
def clean_text(text):
    if isinstance(text, str):  # Check if 'text' is string instance
        cleaned_text = re.sub(r'[^\s\d\w]', '', text)  # 특수문자 제거
        return cleaned_text
    else:
        return ''

# 한국어 불용어 설정
korean_stopwords = ['을', '를', '이', '가', '은', '는', '에', '의', '와', '과', '도', '으로', '한', '하다']

# Okt 객체 생성
okt = Okt()

# 토큰화, 어간추출, 불용어 제거
def tokenize_text(text):
    word_tokens = okt.morphs(text)  # 토큰화 및 어간추출
    result = [w for w in word_tokens if not w in korean_stopwords]
    return result

# 전처리를 거쳐 새로운 컬럼에 저장
case_list['clean_판시사항'] = case_list['판시사항'].apply(lambda x: tokenize_text(clean_text(x)))
case_list['clean_판결요지'] = case_list['판결요지'].apply(lambda x: tokenize_text(clean_text(x)))
case_list['clean_참조조문'] = case_list['참조조문'].apply(lambda x: tokenize_text(clean_text(x)))
case_list['clean_참조판례'] = case_list['참조판례'].apply(lambda x: tokenize_text(clean_text(x)))
case_list['clean_판례내용'] = case_list['판례내용'].apply(lambda x: tokenize_text(clean_text(x)))

case_list.drop(['판시사항', '판결요지', '참조조문', '참조판례', '판례내용'], axis=1, inplace=True)

# CSV 파일로 저장
case_list.to_csv('교통사고_전처리.csv', index=False)
