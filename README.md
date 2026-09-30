<a href="https://plus.cnu.ac.kr/"><img align="right" src="assets/cnu-logo.svg" width="48" alt="Chungnam National University"></a>

<h1>동남권 수질오염도 추세 분석</h1>

<p>Water Quality Trends in Southeastern Korea (Busan, Ulsan, Gyeongsangnam-do)</p>

<p>
  2024년 소프트중심대학 소프트웨어중점사업단 교양수업인 "컴퓨터과학적사고" 강의에서 본인이 제출한 과제입니다.<br>
  This assignment was submitted for "Computational Scientific Thinking", a general-education course offered through the National Center of Excellence in Software at Chungnam National University in 2024.
</p>

---

## 목차

<table>
  <thead>
    <tr>
      <th>구분</th>
      <th>목차</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>데이터 분석 주제</th>
      <td><a href="#data-analysis-topic">데이터 분석 주제</a></td>
    </tr>
    <tr>
      <th rowspan="4"><a href="#code-development-process">코드 개발 과정</a></th>
      <td><a href="#regional-data-extraction">CSV 파일에서 지역별 데이터를 추출</a></td>
    </tr>
    <tr>
      <td><a href="#file-separation">각 지점별 데이터를 분리하여 저장</a></td>
    </tr>
    <tr>
      <td><a href="#graphing">각각의 파일을 읽어 그래프로 나타내는 코드</a></td>
    </tr>
    <tr>
      <td><a href="#web-based-file-selection">HTML 웹 기반 파일 선택</a></td>
    </tr>
    <tr>
      <th>코드 구조</th>
      <td><a href="#code-structure">코드 구조</a></td>
    </tr>
    <tr>
      <th>주제에 대한 결론</th>
      <td><a href="#conclusion">주제에 대한 결론</a></td>
    </tr>
    <tr>
      <th>과제를 통한 고찰</th>
      <td><a href="#reflection">과제를 통한 고찰</a></td>
    </tr>
  </tbody>
</table>

---

<a id="data-analysis-topic"></a>

## 1. 데이터 분석 주제
2016 - 2019년도에 ‘2차 하수 처리 탱크를 이용한 폐수정화처리’라는 프로젝트를 수행한 적이 있다. 이 프로젝트는 미생물이 가진 효소의 입체구조를 생화학적으로 분석하여 효소의 활성화율을 측정하고, 미생물의 최적 배양환경을 찾아내어 영역별 배치될 2차 하수 처리 탱크를 고안하여 수질을 정화하는 것이다.

이 실험을 하는 도중 할 일 중 하나는 오염도가 높고 부영양화가 심한 지점을 찾는 것이었다. 자연환경에 대한 정보를 얻어야 하는데, 날씨나 주변 환경에 따라 목표 지점의 오염도가 달라지는일이 많아서 오염 지점을 선정하는 데 어려움이 있었다. 또한 평균 오염도가 높은 지점에서 실험하는 것이 실험 결과의 신뢰도를 높이는 방법인데, 순간의 오염도로는 실험의 신뢰성을 담보할 수 없어 애를 먹은 적이 있다.

이 프로젝트와 균주로 후속 실험을 진행하려고 하는데, 마침 과제에 원하는 장기 오염 추세 국가 제공 데이터를 분석할 수 있는 기회가 있어 각 하천의 수질오염도 데이터를 분석하여 후속 실험의 밑거름으로 삼을 수 있도록 한다. 자료는 한국환경연구원의 환경영향평가 수질정보 (2024.01.11.)를 이용하였다. CSV 데이터 중 실제 실험에서 사용되었던 비교군인 경상남도, 부산광역시, 울산광역시의 자료만을 이용하였다.

<a id="code-development-process"></a>

## 2. 코드 개발 과정
코딩 과정은 다음과 같다.

1. CSV 파일에서 경상남도, 부산광역시, 울산광역시 관련 데이터를 추출한다.
2. 각 지점별 데이터를 한 디렉터리에 분리하여 저장한다.
3. 각각의 파일을 읽어 그래프로 나타낼 수 있는 코드를 작성한다.
4. HTML 웹 기반으로 각 파일을 선택할 수 있도록 하고, 이를 3.과 연결한다.

<a id="regional-data-extraction"></a>

#### 1. CSV 파일에서 경상남도, 부산광역시, 울산광역시 관련 데이터를 추출한다.

<table>
  <thead>
    <tr>
      <th>지역</th>
      <th>포함된 검색어</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://www.busan.go.kr/"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Symbol_of_Busan_(2023%E2%80%93).svg" height="30" alt="부산광역시"></a><br>
        부산광역시<br>
        <sub>(부산시, 부산)</sub>
      </td>
      <td>
        <img src="assets/municipal/busan-dongnae.svg" width="18" height="18" alt=""> 동래구 ·
        <img src="assets/municipal/busan-geumjeong.svg" width="18" height="18" alt=""> 금정구 ·
        <img src="assets/municipal/busan-yeonje.svg" width="18" height="18" alt=""> 연제구 ·
        <img src="assets/municipal/busan-gangseo.svg" width="18" height="18" alt=""> 강서구
        <br>
        <img src="assets/municipal/busan-gijang.svg" width="18" height="18" alt=""> 기장군 ·
        <img src="assets/municipal/busan-namgu.svg" width="18" height="18" alt=""> 남구 ·
        <img src="assets/municipal/busan-donggu.svg" width="18" height="18" alt=""> 동구 ·
        <img src="assets/municipal/busan-busanjin.svg" width="18" height="18" alt=""> 부산진구
        <br>
        <img src="assets/municipal/busan-bukgu.svg" width="18" height="18" alt=""> 북구 ·
        <img src="assets/municipal/busan-sasang.svg" width="18" height="18" alt=""> 사상구 ·
        <img src="assets/municipal/busan-saha.svg" width="18" height="18" alt=""> 사하구 ·
        <img src="assets/municipal/busan-seogu.svg" width="18" height="18" alt=""> 서구
        <br>
        <img src="assets/municipal/busan-suyeong.svg" width="18" height="18" alt=""> 수영구 ·
        <img src="assets/municipal/busan-yeongdo.svg" width="18" height="18" alt=""> 영도구 ·
        <img src="assets/municipal/busan-junggu.svg" width="18" height="18" alt=""> 중구 ·
        <img src="assets/municipal/busan-haeundae.svg" width="18" height="18" alt=""> 해운대구
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://www.ulsan.go.kr/"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_Ulsan.svg" height="24" alt="울산광역시"></a><br>
        울산광역시<br>
        <sub>(울산시, 울산)</sub>
      </td>
      <td>
        <img src="assets/municipal/ulsan-donggu.svg" width="18" height="18" alt=""> 동구 ·
        <img src="assets/municipal/ulsan-junggu.svg" width="18" height="18" alt=""> 중구 ·
        <img src="assets/municipal/ulsan-namgu.svg" width="18" height="18" alt=""> 남구 ·
        <img src="assets/municipal/ulsan-bukgu.svg" width="18" height="18" alt=""> 북구 ·
        <img src="assets/municipal/ulsan-ulju.svg" width="18" height="18" alt=""> 울주군
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://www.gyeongnam.go.kr/"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_South_Gyeongsang_Province.png" height="24" alt="경상남도"></a><br>
        경상남도<br>
        <sub>(경남)</sub>
      </td>
      <td>
        <img src="assets/municipal/gyeongnam-changwon.svg" width="18" height="18" alt=""> 창원시 (의창구, 성산구, 마산합포구, 마산회원구, 진해구)
        <br>
        <img src="assets/municipal/gyeongnam-gimhae.svg" width="18" height="18" alt=""> 김해시 ·
        <img src="assets/municipal/gyeongnam-yangsan.svg" width="18" height="18" alt=""> 양산시 ·
        <img src="assets/municipal/gyeongnam-jinju.svg" width="18" height="18" alt=""> 진주시 ·
        <img src="assets/municipal/gyeongnam-geoje.svg" width="18" height="18" alt=""> 거제시
        <br>
        <img src="assets/municipal/gyeongnam-tongyeong.svg" width="18" height="18" alt=""> 통영시 ·
        <img src="assets/municipal/gyeongnam-sacheon.svg" width="18" height="18" alt=""> 사천시 ·
        <img src="assets/municipal/gyeongnam-miryang.svg" width="18" height="18" alt=""> 밀양시 ·
        <img src="assets/municipal/gyeongnam-haman.svg" width="18" height="18" alt=""> 함안군
        <br>
        <img src="assets/municipal/gyeongnam-geochang.svg" width="18" height="18" alt=""> 거창군 ·
        <img src="assets/municipal/gyeongnam-changnyeong.svg" width="18" height="18" alt=""> 창녕군 ·
        <img src="assets/municipal/gyeongnam-goseong.svg" width="18" height="18" alt=""> 고성군
        <br>
        <img src="assets/municipal/gyeongnam-hadong.svg" width="18" height="18" alt=""> 하동군 ·
        <img src="assets/municipal/gyeongnam-namhae.svg" width="18" height="18" alt=""> 남해군 ·
        <img src="assets/municipal/gyeongnam-hapcheon.svg" width="18" height="18" alt=""> 합천군 ·
        <img src="assets/municipal/gyeongnam-hamyang.svg" width="18" height="18" alt=""> 함양군
        <br>
        <img src="assets/municipal/gyeongnam-sancheong.svg" width="18" height="18" alt=""> 산청군 ·
        <img src="assets/municipal/gyeongnam-uiryeong.svg" width="18" height="18" alt=""> 의령군
      </td>
    </tr>
  </tbody>
</table>

CSV 파일의 D행이 지역 정보를 담고 있으므로, 아래 기초자치단체 검색어가 포함된 열만을 선택한다. 이후 D행의 각 열이 동일한 것끼리 나누어서 저장한다. 이때 G행의 차수가 1~3개밖에 없는 데이터는 수질오염도의 추이를 분석하기 부족하므로 제외한다. 중구, 서구, 북구, 동구, 남구, 강서구, 고성군은 동명의 기초자치단체가 있어 해당 광역자치단체 검색어와 조합하여 검색하였다.

<a id="file-separation"></a>

#### 2. 각 지점별 데이터를 한 디렉터리에 분리하여 저장한다.
원본 자료를 엑셀의 기본값 설정에 맞게 직접 짠 euckrconverterforwindows.py를 이용하여 euc-kr로 변환하였다. 이후 파일을 저장할 때는 to-csv() 함수의 encoding 요소의 기본값이 UTF-8이라 윈도우 엑셀 환경에서 인코딩이 깨져 원활하게 인식할 수 없으므로 앨리스 실습 때와 동일하게 인코딩 형식을 지정 (euc-kr)하여 해결하였다.

인코딩이 어떻게 되어 있는지 주어진 디렉터리 내의 파일을 열어 리스트에 존재하는 인코딩 방식을 적용해보고, 오류가 생기면 다음에 존재하는 인코딩 방식으로 순차적으로 열어보도록 작성하였다. 이후 엑셀의 기본 설정인 EUC-KR 인코딩으로 파일을 저장하였고, 이 파일의 목적은 파일을 분리하기 전 같은 인코딩 방식으로 통일하는 것이다.

<a id="graphing"></a>

#### 3. 각각의 파일을 읽어 그래프로 나타낼 수 있는 코드를 작성한다.

<a id="web-based-file-selection"></a>

#### 4. HTML 웹 기반으로 각 파일을 선택할 수 있도록 하고, 이를 3.과 연결한다.

동적으로 이미지가 표현되어야 하나 위의 코드는 정적 코드이기 때문에 새로고침을 하고 다른 데이터를 불러와도 똑같은 이미지가 표현된다.

<a id="code-structure"></a>

## 코드 구조

```text
CNUcompthink24/
├── dividefiles.py                 지역별 수질조사 CSV 추출 및 분리
├── euckrconverterforwindows.py    CSV 파일의 EUC-KR 인코딩 변환
├── main.py                        Flask 기반 파일 선택 및 COD·BOD 그래프 생성
├── static/
│   └── output_graphs/             생성된 그래프 저장 경로
└── assets/
    └── cnu-logo.svg               README 표지 로고
```

<a id="conclusion"></a>

## 3. 주제에 대한 결론
1번의 데이터 분석 주제의 데이터 분석 선정 이유에 따르면 날씨 또는 주변 환경에 따른 편차가 없어야 하는 조건 첫 번째는 그래프의 데이터 추세가 일정한가 (추세의 편차가 들쭉날쭉하지 않은가)이며, 두 번째는 절대적인 BOD, COD 수치가 실험에서 유의미한 변화를 이끌어낼 수 있을 만큼 높은가였다. (절대적인 수치가 높지 않으면 깨끗한 물에서 수질정화를 해도 변화가 일어나지 않는다.) 그래프를 분석하니 거제시 하청면 석포리 69번지(폐기물 매립장) 앞의 COD, BOD 데이터가 원하는 데이터에 가장 부합한 것을 알 수 있었다.

<a id="reflection"></a>

## 4. 과제를 통한 고찰
데이터 분석하기에 앞서 데이터의 특징이 무엇인지, 데이터의 종류가 무엇인지에 대한 인지가 선행되어야 제대로 된 데이터분석을 진행할 수 있다는 것을 더욱 실감하게 되었다. 그 데이터의 특성을 분석하는 것은 결국 사람이 직접 해야 하는 영역이고 방향성은 사람이 결정해야 하는 것을 알았다.

정부 공공 데이터 포털에서 정보를 다운받았을 때, 여러 속성이 CSV파일 내에 존재하였으나 조사기관이 서로 다른 데이터를 모두 취합한 것에 불과해서 모든 데이터가 정형화되어 존재하지 않았다. AI를 이용하여 데이터를 분석하기 전 데이터를 가공하는 과정에서 시간이 많이 소모되었는데, 위의 코드를 수정하는 시행착오의 과정에서 하나라도 데이터의 정제 및 취사선택이 진행되지 않으면 이후 데이터가 분석되지 않거나, 이상치가 출력되는 등의 결과가 나타나게 되었다. 데이터의 가공도 중요하지만 데이터를 정제하여 분석에 알맞게 쓸 수 있도록 하는 과정인 데이터 분석도 가공 못지않게 중요하거나 더 중요할 수 있겠다는 생각을 하였다.

<br>

<sub>본 문서에 사용된 학교·지자체 로고 및 기타 이미지는 각 권리자에게 귀속되며, 관련 기관·자료의 식별과 과제 설명을 위한 목적으로만 사용하였다.</sub>
