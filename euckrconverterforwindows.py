import os
import pandas as pd

input_dir = 'directory'

files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for file_name in files:
    file_path = os.path.join(input_dir, file_name)
    success = False
    
    # 가능한 인코딩 목록
    encodings = ['cp949', 'utf-8', 'latin1']

    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)

            # euc-kr 인코딩으로 파일 저장
            df.to_csv(file_path, encoding='euc-kr', index=False)
            print(f'Successfully converted {file_name} to EUC-KR using {encoding} encoding.')
            success = True
            break
        
        except Exception as e:
            print(f'Failed to process {file_name} with {encoding} encoding: {e}')
    
    if not success:
        print(f'Could not convert {file_name} to EUC-KR. Please check the file encoding.')