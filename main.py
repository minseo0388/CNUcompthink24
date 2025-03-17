import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template_string, request
import uuid

# GUI 백엔드 비활성화
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

# 데이터 디렉터리 설정
input_dir = 'refined_data'
output_dir = os.path.join(app.root_path, 'static', 'output_graphs')  # 정적 디렉터리 설정
os.makedirs(output_dir, exist_ok=True)  # 디렉터리 생성

# HTML 템플릿
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>파일 선택</title>
</head>
<body>
    <h1>파일 선택</h1>
    <form method="POST">
        <label for="file">파일 선택:</label>
        <select name="file" id="file">
            {% for file in files %}
                <option value="{{ file }}">{{ file }}</option>
            {% endfor %}
        </select>
        <button type="submit">확인</button>
    </form>
    {% if graph_path %}
        <h2>그래프</h2>
        <img src="{{ graph_path }}" alt="그래프">
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    graph_path = None

    if request.method == 'POST':
        file_name = request.form.get('file')  # 안전하게 값 가져오기
        if file_name:
            file_path = os.path.join(input_dir, file_name)

            if os.path.exists(file_path):
                # 파일 읽기
                df = pd.read_csv(file_path)

                # 유효 데이터 필터링
                if {'조사차수값(IVSTG_ODR_VAL)', '화학적산소요구량(COD_VAL)', '생물화학적산소요구량(BOD_VAL)'}.issubset(df.columns):
                    valid_data = df.dropna(subset=['조사차수값(IVSTG_ODR_VAL)', '화학적산소요구량(COD_VAL)', '생물화학적산소요구량(BOD_VAL)'])
                    valid_data = valid_data[(valid_data['화학적산소요구량(COD_VAL)'] >= 0) & (valid_data['생물화학적산소요구량(BOD_VAL)'] >= 0)]

                    # 그래프 생성
                    plt.figure(figsize=(10, 6))
                    plt.plot(valid_data['조사차수값(IVSTG_ODR_VAL)'], valid_data['화학적산소요구량(COD_VAL)'], label='COD', marker='o')
                    plt.plot(valid_data['조사차수값(IVSTG_ODR_VAL)'], valid_data['생물화학적산소요구량(BOD_VAL)'], label='BOD', marker='s')

                    plt.title(f'COD and BOD vs IVSTG_ODR_VAL - {file_name}')
                    plt.xlabel('Investigation Order (IVSTG_ODR_VAL)')
                    plt.ylabel('Values')
                    plt.legend()
                    plt.grid(True)

                    # 그래프 저장
                    temp_filename = f'{uuid.uuid4().hex}.png'
                    graph_path = os.path.join(output_dir, temp_filename)
                    plt.savefig(graph_path)
                    plt.close()

                    # 웹 경로 반환
                    graph_path = f'/static/output_graphs/{temp_filename}'

                    return render_template_string(HTML_TEMPLATE, files=files, graph_path=graph_path)

                return '데이터가 잘못되었습니다.'  # 데이터 유효성 실패

            return '파일이 존재하지 않습니다.'  # 파일 경로 없음

        return '파일이 선택되지 않았습니다.'  # 파일 미선택

    return render_template_string(HTML_TEMPLATE, files=files, graph_path=graph_path)

if __name__ == '__main__':
    app.run(debug=True)
