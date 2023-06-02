import pandas as pd
from ast import literal_eval
from keras.preprocessing.text import Tokenizer

# 데이터 불러오기
case_list = pd.read_csv('교통사고_전처리_정리완.csv', encoding='utf-8')

# 'clean_판결요지' 컬럼의 모든 행에 대해 문자열을 리스트로 변환
case_list['clean_판결요지'] = case_list['clean_판결요지'].apply(literal_eval)

# 모든 행의 리스트를 하나의 리스트로 합치기
text_list = sum(case_list['clean_판결요지'].tolist(), [])

# Tokenizer 객체 생성
tokenizer = Tokenizer()

# 텍스트 데이터에 대해 학습
tokenizer.fit_on_texts(text_list)

# 텍스트를 정수로 변환
# sequences = tokenizer.texts_to_sequences(text_list)


print(tokenizer.word_counts)