import os
import pandas as pd

# 조건에 해당하는 지역 리스트
regions = [
    '부산광역시', '울산광역시', '경상남도', '부산', '울산', '경남', '부산시', '울산시', '창원시', '진주시', '통영시', '사천시',
    '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군',
    '거창군', '합천군', '의창구', '진해구', '성산구', '마산회원구', '마산합포구', '중구', '서구', '동구', '영도구', '부산진구',
    '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구', '기장군', '울주군'
]

# 입력 및 출력 디렉터리 설정
input_file = 'D:/Desktop/새 폴더 (2)/수질_조사_20231222.csv'  # 입력 파일 경로 설정
output_dir = 'D:/Desktop/새 폴더 (2)/refined_data'  # 출력 디렉터리 설정
os.makedirs(output_dir, exist_ok=True)

# CSV 파일 불러오기
# 'utf-8' 인코딩으로 변경하여 시도
df = pd.read_csv(input_file, encoding='utf-8')

# D행 필터링
filtered_df = df[df['조사지점 주소(IVSTG_LC)'].astype(str).str.contains('|'.join(regions))]

# D행을 기준으로 그룹화
grouped = filtered_df.groupby('조사지점 주소(IVSTG_LC)')

# 각 그룹 저장 및 조건에 따라 삭제
for name, group in grouped:
    if 1 <= group['조사차수값(IVSTG_ODR_VAL)'].nunique() <= 3:  # G행의 고유값 개수 조건
        continue  # 조건에 맞지 않으면 저장하지 않음
    output_path = os.path.join(output_dir, f'{name}.csv')
    group.to_csv(output_path, index=False, encoding='euc-kr')

print("처리 완료!")