import pandas as pd
from ast import literal_eval

# 데이터 불러오기
case_list = pd.read_csv('교통사고_전처리.csv', encoding='utf-8')
case_list = case_list.drop('판례상세링크', axis=1)
# 각 컬럼에 대해 빈 리스트([])를 가진 행 제거
for column in ['clean_판시사항', 'clean_판결요지', 'clean_참조조문', 'clean_참조판례', 'clean_판례내용']:
    # 문자열을 리스트로 변환
    case_list[column] = case_list[column].apply(literal_eval)
    # 빈 리스트가 아닌 행만 선택하여 다시 할당
    case_list = case_list[case_list[column].apply(len) > 0]
# 데이터 저장
case_list.to_csv('교통사고_전처리_정리완.csv', index=False)
