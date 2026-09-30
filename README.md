<h1>
  <a href="https://plus.cnu.ac.kr/"><img src="assets/cnu-logo.svg" width="38" alt="Chungnam National University"></a>
  ctl_24
</h1>

<p>
  computational thinking<br>
  2024년 소프트중심대학 소프트웨어중점사업단 교양수업에서 본인이 제출한 과제입니다.
</p>

---

## 목차

1. [데이터 분석 주제](#data-analysis-topic)
2. [코드 개발 과정](#code-development-process)
   - [CSV 파일에서 지역별 데이터를 추출](#regional-data-extraction)
   - [각 지점별 데이터를 분리하여 저장](#file-separation)
   - [각각의 파일을 읽어 그래프로 나타내는 코드](#graphing)
   - [HTML 웹 기반 파일 선택](#web-based-file-selection)
3. [코드 구조](#code-structure)
4. [주제에 대한 결론](#conclusion)
5. [과제를 통한 고찰](#reflection)

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

### 1. CSV 파일에서 경상남도, 부산광역시, 울산광역시 관련 데이터를 추출한다.

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
        부산광역시
      </td>
      <td>
        <a href="https://www.bsjunggu.go.kr/"><img src="https://i.namu.wiki/i/1eNKiEYdrzrkiZ9YcdirKPgz1p7YLpl1NOvZrDb-bKZj5Xo2DwHYGkyiGyCoSSHswA4vi4UGEOLVgdTjWfdl036stfkcNMUunupMM-1WTmuIY65X9CXLdNHZDDnGUjxM84z3FCfV7o5AOAmdxeQFHA.svg" width="18" height="18" alt="중구"> 중구</a> ·
        <a href="https://www.bsseogu.go.kr/"><img src="https://i.namu.wiki/i/2EwFUj4Hhhl-LWHrXKPfVH4oqS9QFdMJV_fJY9KK73pef8wZAm120KQ9Bgph9obAn6PVs0PbbTz9IrJxDQ5F7mxE8PdeqGK1u9WsxbfRIpAyB3SWs2WiRqm1gmUFh9kil-qa1BZGOtRYgiu4ndeUVA.svg" width="18" height="18" alt="서구"> 서구</a> ·
        <a href="https://www.bsdonggu.go.kr/"><img src="https://i.namu.wiki/i/YEiLH0d3aJasNinQWfjyELZXw2KfTJ2XXJOjT0BqFtls5pHwDORLZw0I3GF1eXeV6X7n68GqJWNvgbHJciMo_eIQ3CmUZY8oqYSztmtHTnUp52U9T63Q0vaWyRfK6Woohym6SI4fUzxZV5BZzUBTNA.svg" width="18" height="18" alt="동구"> 동구</a> ·
        <a href="https://www.yeongdo.go.kr/"><img src="https://i.namu.wiki/i/-BJQHEML0ohIF3ozC3kYqailNu-3A2rumCIuM_j7UmQjozp6FtCK48bmb4exOeW22EbJjwhCtmGS7qXPQf4L68ZlRy54U6Kl1teua3r18ESYZpax1oC18r5zlXDb6saeQfRODyFvLTCRUzsnyQFH-w.svg" width="18" height="18" alt="영도구"> 영도구</a>
        <br>
        <a href="https://www.busanjin.go.kr/"><img src="https://i.namu.wiki/i/UPuy4V0__QbLX6fSN6yxCvtLzUSDN1OJpCeXuzFHfId5tC50WoD4ZFSd55CUhpoBNe8yPU4zS4AWQBh-A_nAnJ23vvdADSxc-39Hr3pQr6bT0KyY7js0CTgq9DFtpRXBz6r0W4X83xcC_vb2M9tA7A.svg" width="18" height="18" alt="부산진구"> 부산진구</a> ·
        <a href="https://www.dongnae.go.kr/"><img src="https://i.namu.wiki/i/3a0Yqas0bTm3rvaEXsWdcPyd2RU5FIOeuw2NB-1Ct9UoyBfhgvlJE4velWZNd4rwpkYVcQ71JjWskfLHFHOdO_JgK-bE5TOOVPcHtTQ6z-PfuLEt8EKI9RJVy_sw9tNKf43n81P_JJmsBAp2B4Q_Fg.svg" width="18" height="18" alt="동래구"> 동래구</a> ·
        <a href="https://www.bsnamgu.go.kr/"><img src="https://i.namu.wiki/i/dy5ZwKu_kqSVnrpBlSIC4KJOcxIB7ETgQecyeTufxTWQEDsGTOlShFe5snApi9sJoNBLM0jmgi_TqDYgTCTixlxL3vLCi54agURySajzRglBJo7E5pfo4f7X9UMRIPcQfe0-5fuc3jJCPhw0CCUBjA.svg" width="18" height="18" alt="남구"> 남구</a> ·
        <a href="https://www.bsbukgu.go.kr/"><img src="https://i.namu.wiki/i/YlPuKcFv0BVgf3EOvn16GhTtmxADKl_QL4kewjq13NZ3_OUvvVg3Wfe25vEo7l_oYuoeTdh6z4TV7NjGlI1LiVKFNTj2x8FhEx6VTcHwCjKeX-GKccMQxF5VdppkwojbV5sY7PDuKUv5JeCLP4OpxA.svg" width="18" height="18" alt="북구"> 북구</a>
        <br>
        <a href="https://www.haeundae.go.kr/"><img src="https://i.namu.wiki/i/YlPuKcFv0BVgf3EOvn16GhTtmxADKl_QL4kewjq13NZ3_OUvvVg3Wfe25vEo7l_oYuoeTdh6z4TV7NjGlI1LiVKFNTj2x8FhEx6VTcHwCjKeX-GKccMQxF5VdppkwojbV5sY7PDuKUv5JeCLP4OpxA.svg" width="18" height="18" alt="해운대구"> 해운대구</a> ·
        <a href="https://www.saha.go.kr/"><img src="https://i.namu.wiki/i/xiry9OTwBF0V5f_gndLD3JDLFiVLKCAEE19xNtWZKJkbtpssCOduw6nRSknJAElAV_A8ylyyUJNNHiqZW790J7cPGOvbH04wdiCMYwjT9oI7LQXiTRbd5_6iF6ARUdcSdzVtBdDAI2r2wULhCYurWg.svg" width="18" height="18" alt="사하구"> 사하구</a> ·
        <a href="https://www.geumjeong.go.kr/"><img src="https://i.namu.wiki/i/ejVPCgpEK51ZkKY6wNkZtwfbdcubTQv3QqVl12QQM0UZ0i0zEhNd6ns0Eqt5m8tPOlqiQ8WSmSRK0osksC4LjYmOxWPu9HEV7QtxxKfHuVssd_PmNxioJHUTgyriBBZ7BPrXbRU3POIfacZqR-mCPQ.svg" width="18" height="18" alt="금정구"> 금정구</a> ·
        <a href="https://www.bsgangseo.go.kr/"><img src="https://i.namu.wiki/i/ARdlKU4tnOsn-K5HjP890bJkgmAkv_2yuHmafysEa0qF7sXYtZUGTG4L719o7w1XlMYTPGcjcalu_Q_hJwKhIBp6lYAjudVbn40TKYIErmcQmHO4BLQjuub84CYysWSK_DawMT2tlTtM7oFTKZyj-g.svg" width="18" height="18" alt="강서구"> 강서구</a>
        <br>
        <a href="https://www.yeonje.go.kr/"><img src="https://i.namu.wiki/i/nk6U8fTkx_9m73YQGGyrinnyFH0ibYHChYVsQCxbg3VZ_jwy4h5y14-K2rqS0l57vwFfrEej3QohSsQujytu4ciS03SqKb46iBxTbFYcz-7BXtoSN_l8a75musZ6z0WG1u_MtW6Jtow4g_iGF9Ks5A.svg" width="18" height="18" alt="연제구"> 연제구</a> ·
        <a href="https://www.suyeong.go.kr/"><img src="https://i.namu.wiki/i/IVmH1M50bvlyo4kruYXnzSk1oez5dfLkCttHcSCozBjYUhAaITUV44eG82ox5GEKZMVPDSEHqe0JAhnqb8BL25fneUYwFk0EVLLvgvRUgEqEKc1Vbek4DntTPdGPXWgcOhDnqbPJi5Boj2leUfZf-w.svg" width="18" height="18" alt="수영구"> 수영구</a> ·
        <a href="https://www.sasang.go.kr/"><img src="https://i.namu.wiki/i/pAJAKKmzoEGkP-7z2AfajYxD-nsjL_1Du3lCtjJa6mOu7MQfiX6LMEsd7QwWNftXT8-SJaPNpTNQL8JfX5ersE4bawWIHD9kpGk9nyPsYAAjl8jVMLdo-q4EnrnaETp1QTmzBu_BGwA0L-YK9Qb3wA.svg" width="18" height="18" alt="사상구"> 사상구</a> ·
        <a href="https://www.gijang.go.kr/"><img src="https://i.namu.wiki/i/Sx4wG5Rg9GrNtjKCm17cQxJbcEr8bonHJQAKE_ZM49QJY3PyGrrXpglEPZWwyV7QQsvDJ9rjAK2ov4CIpsg8MhBMCzh8LyIkoauIGM9QPtUSgPvS9TVS_zdPKL-Uc1aJe2ndnseMhkp1kZbc4uxvRw.svg" width="18" height="18" alt="기장군"> 기장군</a>
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://www.ulsan.go.kr/"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_Ulsan.svg" height="24" alt="울산광역시"></a><br>
        울산광역시
      </td>
      <td>
        <a href="https://www.junggu.ulsan.kr/"><img src="https://i.namu.wiki/i/zWPrX0pH4zyQ25jQZhL6_-TzyclxTNCecWWoWnQXcH9Eb4WHLgkFHL67y19xegga0NjCBGOwK93Fwud8kc3dUqHbVSEH8fIUbIz86ZWvy8BvkEu0QI5j7B-nc9y2cNmFEWIKqHyyuj8vg4aI1KAQdA.svg" width="18" height="18" alt="중구"> 중구</a> ·
        <a href="https://www.ulsannamgu.go.kr/"><img src="https://i.namu.wiki/i/i5XO8XJSI1X2MmEBuH81vAdHJnLA6CukJ4OnZ-HPJ-6PG_QKIYWYD0sFh4JkaCjyBq31otGVl1dLINZiM91g_BEQ5Z0lPcmAiwqOFxAILTx6REtPsdjn0OHJo09ckzc3IY_dWLOUjsyWHYiGPLB59w.svg" width="18" height="18" alt="남구"> 남구</a> ·
        <a href="https://www.donggu.ulsan.kr/"><img src="https://i.namu.wiki/i/TsLOMtnwoLXCsiztrX6LS_ZVgHZoSnWKPAc4P8dDtcvyUkj04LtOkrneynJGQXX7F0pqPUmT2PfShOoEZadVTZou_r_fVLHo6H3PrsX7_07E88jIvOan2vJIS8cjYN7WpuUXFhxiJcvCyY33uuJvFQ.svg" width="18" height="18" alt="동구"> 동구</a> ·
        <a href="https://www.bukgu.ulsan.kr/"><img src="https://i.namu.wiki/i/sgt1vbF5iLQvYIHnt-p6UZUXOQ00FRsqbhbdmS8Umzyu3ABZ-_PaECK0s7mfXd9iXgVIXDQ0QetmxviKVY8sDA_DmVsjF4jKxqch8dA_qvCCa5E22q_mhd54OW8SaASHotmm_y2592jxQcJWS33xTg.svg" width="18" height="18" alt="북구"> 북구</a> ·
        <a href="https://www.ulju.ulsan.kr/"><img src="https://i.namu.wiki/i/WwIVb8-6U3729DdXtLvNvD-Worh8z360VFAEu6RVOrIF_4Mfrh17XtXCd2PNADagf8mqhMLKcNfYmTsOaexlXCDjpv1nOgyIdkxxsgSrAyRMyl_GHkNKJJkfggRowMnTLBXjy8MH0OPdRTO9PfAp2A.svg" width="18" height="18" alt="울주군"> 울주군</a>
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://www.gyeongnam.go.kr/"><img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Emblem_of_South_Gyeongsang_Province.png" height="24" alt="경상남도"></a><br>
        경상남도
      </td>
      <td>
        <a href="https://www.changwon.go.kr/"><img src="https://i.namu.wiki/i/4tm1m8U_zzuN5k8xXhhnMUxqtzZ2deun3i-fOnywpNu5iPrEd2Jgc378QMBkT9xUGIqXe0WV6qHirVNRkq5dfuGZxz-hCQBh3XroOeHmg41BUjOB4l19xCJ0YU8MpcAzl3mZvVJBHl3x-_I34ygECQ.svg" width="18" height="18" alt="창원시 (의창구, 성산구, 마산합포구, 마산회원구, 진해구)"> 창원시 (의창구, 성산구, 마산합포구, 마산회원구, 진해구)</a>
        <br>
        <a href="https://www.jinju.go.kr/"><img src="https://i.namu.wiki/i/u-XDyn8iJF-BdhcMAzqaQmzZB2OWO7OfS14WtiC_cFEOyMm4L4SdxRWRHqKYzMHgGMDCyh22noxWeARkFHedzQ.svg" width="18" height="18" alt="진주시"> 진주시</a> ·
        <a href="https://www.tongyeong.go.kr/"><img src="https://i.namu.wiki/i/qWNvK2T_TbqtecJQJl9sjAGq27rdqT48fC-_TpN2kIVLD2cx-U5zD09ongO6RF1ku8SBJWBDxG-9K0e-f0GQvzaXdJRACVFilY9XfDXy2Iu7VT1drA0b1DLBDZYGkilP1LTpYw_uzfH70gYyqf93Lg.svg" width="18" height="18" alt="통영시"> 통영시</a> ·
        <a href="https://www.sacheon.go.kr/"><img src="https://i.namu.wiki/i/5p5B2i6F0BzZNXrsrtHBGXyCbiWhQPbPTDQbZ4igUGQPTR_E_hR-Ng18P55Igp_b_JKbSVEsztkNAqDqrnx5peW_cARGTgB2WPVAOUgkB7_KM8buLNxbYz4Y3DAFB9ssynqwRZ-S6MdgRtiRR4TcjQ.svg" width="18" height="18" alt="사천시"> 사천시</a> ·
        <a href="https://www.gimhae.go.kr/"><img src="https://i.namu.wiki/i/QFRExYIbdHOptQ-F5l3wszM4UzGLA6N6mD0IPghR0hCrl06MzfwyGPbFOlaXuEFeGe6Ao_JZz22absZPB7tr1rLlFd8v3xgNb7i2F4aiXnz6mu6ZPh4DPo4fNBczAZ2nJoPzO_ozuCXno53v2cimrw.svg" width="18" height="18" alt="김해시"> 김해시</a>
        <br>
        <a href="https://www.miryang.go.kr/"><img src="https://i.namu.wiki/i/tQRCX2PAP-GAtpz13OQPssFID4POOoPCSGl03Wr9RtQQPiPix0ZkPufVAJCQVmgMiYvTj2ZSU88GkqQ6RnBDLxza8P0qV32wQFQk1qyC9NC28En1iSLrq1-n5oormSQyDn9xSWnsvEcuK8WmqIijEw.svg" width="18" height="18" alt="밀양시"> 밀양시</a> ·
        <a href="https://www.geoje.go.kr/"><img src="https://i.namu.wiki/i/FnJEcAZXTj33GCDWU0aE-I08N1gr0XgzlQKtcxZzucjgu7snWuQdnyHYA4XJG1AIvJ4l9WfFQ2TYb9DCP3wXSnBbLjae3Lzm87WGYbvQJF1DC0ecfke9RQujvPZX1E_MHAWBVWKe9HPdRHHOIc-tVQ.svg" width="18" height="18" alt="거제시"> 거제시</a> ·
        <a href="https://www.yangsan.go.kr/"><img src="https://i.namu.wiki/i/5njPL5VcelP6N7EQjzbKuRNPtVZ0AL86bqRo3V6N_fp-DFZW4NFHIrYrRouQWXyKmnb4vMmSTldxPhC9JW6aO_Ozaq9vTt1Pb60LC8iuiI9Keldrq2vnd1_5qqHqz7LhOMllnEIAXVUljj8rLoIRow.svg" width="18" height="18" alt="양산시"> 양산시</a>
        <br>
        <a href="https://www.uiryeong.go.kr/"><img src="https://i.namu.wiki/i/35ASobQHS2Cgzh3rW2Gr4Ilk_703XQA8PA3qJcCX9yC4sSZ-A-6OgWTjTO_Rggy3ygppnRWabTFl3GdoopH3pITcq2rgiSfuYPo4e_-nbEIy-9-STFHQn_OiC0omHIYsFHue6ezlUFb9Bwiq4FCPeg.svg" width="18" height="18" alt="의령군"> 의령군</a> ·
        <a href="https://www.haman.go.kr/"><img src="https://i.namu.wiki/i/BjV4dD1Go_8SimX7iAmkzuDkWD2dX7LKgZysjc9sD5Kew2zGwiAPvwMDzWzkKh3wmYdu6aw-JnuoIlShZCU9_IO9ZQU-hZYdn0bKwxY-NXo62i4ddQZX81YLlnIcYwSeKVqV7A4pD0zHSWVg008SiA.svg" width="18" height="18" alt="함안군"> 함안군</a> ·
        <a href="https://www.cng.go.kr/"><img src="https://i.namu.wiki/i/_lwhJxWJwjhg-otg1LTqdenJCpq3lxCyJNhUoEBxcA5b9j3X2RSBQBY-zArdcC9U_QY5Rc52r2nCdDLIz7RFNmJ9_tded7LOhuxVCzUrKn7Yn31349qqDA1RIsiS8rhEa5rVBTV2dc3T0FEuNxkhJw.svg" width="18" height="18" alt="창녕군"> 창녕군</a> ·
        <a href="https://www.goseong.go.kr/"><img src="https://i.namu.wiki/i/aCSJVW-PA8rvdKfp2eYFX7Km83NecvHGKknFAyEbG3sYYu5Ql4fJ4SgPin1Po0LVV_tfADQmI40J-kYIwp67eesdy4jsq8iNZqhwsPNSKZfuFq5X8AVujpWdgiUDE1sDcUy80P-Sz2Zj-chVb_BJtA.svg" width="18" height="18" alt="고성군"> 고성군</a>
        <br>
        <a href="https://www.namhae.go.kr/"><img src="https://i.namu.wiki/i/Mny2V8aJg4fqA8aUBHc5tq79Uw5FsEwENl7ZzLx6hlnjjNoFtX1u8JgAED6tpGoTAMEfw_206N-lPHwDHp7h92weEZxVWmDQeRm0FinPUV1j80GMcKsziD7WyjchE3BtLEbnIgUrv3EZrmuFKo3Saw.svg" width="18" height="18" alt="남해군"> 남해군</a> ·
        <a href="https://www.hadong.go.kr/"><img src="https://i.namu.wiki/i/n3xShxR22on2FYr-1uzyxV3lheqJeaUV3ZPh3SJcHUA9H-cNGkPs_w2un-AnDhrChx2M4iJyubRiCLb9AozoN7AX6U9c0KnbMC9OwUCYsWJp54P0BSBUQ4WBL5HlgNNorodZMPawSui8bLxhTntymw.svg" width="18" height="18" alt="하동군"> 하동군</a> ·
        <a href="https://www.sancheong.go.kr/"><img src="https://i.namu.wiki/i/NC1dCsWNENuggYroiIPXRmB2O8eZV12XleWUgXa2r55pvzTFjj4AiDcYzVnObT8guXSaAOcghdhwuTvI7H2QthUfNzR2Q_-mcnPo04DAXqycF5574JXKxVVZy6vEwMyRfmwQFoecSLHmfUFCQz2OrA.svg" width="18" height="18" alt="산청군"> 산청군</a> ·
        <a href="https://www.hygn.go.kr/"><img src="https://i.namu.wiki/i/Y8A7QiTt_Ekbf0wJH2u-yTELhSI5-VB-KAE87JWqt4fduo1rzrcKHX1gzn6pKAF7zBaol0kRif53jq3YjPBKtb4-iie94xR0D2_7RfaElIq6Yn4jsuk01UmZl818epmAlQK7wzyWIuMtwbisGxdbeg.svg" width="18" height="18" alt="함양군"> 함양군</a>
        <br>
        <a href="https://www.geochang.go.kr/"><img src="https://i.namu.wiki/i/ZvR6cPcOt6m4-OC9RgdQXicGlKNOk81BYqpAJdkDIUazjJE-MF4jSi3FgEs4hpbkFeLJkVxL9DsmtlaUokSCS5pDITdXz_Ln6KopZk3Da9ts1gA0rGNuw7q3mk5oZIXtYLClv2Of148Il3I4P1KFeA.svg" width="18" height="18" alt="거창군"> 거창군</a> ·
        <a href="https://www.hc.go.kr/"><img src="https://i.namu.wiki/i/9Vyjl1xF3YnR_AuQ-XZM_JY7BT3xzzBRha6rUlfQxwo6vCfDQqx5WY9HgY4IWIubzulFkJQWm8cRemuFpWCg6kOak9FvIV-I5XaQx3uXC75nzSjVGFAqlmSSfn90T_eZ1P9Qss1nm14rtXbT0emsnQ.svg" width="18" height="18" alt="합천군"> 합천군</a>
      </td>
    </tr>
  </tbody>
</table>

CSV 파일의 D행이 지역 정보를 담고 있으므로, 아래 기초자치단체 검색어가 포함된 열만을 선택한다. 이후 D행의 각 열이 동일한 것끼리 나누어서 저장한다. 이때 G행의 차수가 1~3개밖에 없는 데이터는 수질오염도의 추이를 분석하기 부족하므로 제외한다.

<a id="file-separation"></a>

### 2. 각 지점별 데이터를 한 디렉터리에 분리하여 저장한다.
원본 자료를 엑셀의 기본값 설정에 맞게 직접 짠 euckrconverterforwindows.py를 이용하여 euc-kr로 변환하였다. 이후 파일을 저장할 때는 to-csv() 함수의 encoding 요소의 기본값이 UTF-8이라 윈도우 엑셀 환경에서 인코딩이 깨져 원활하게 인식할 수 없으므로 앨리스 실습 때와 동일하게 인코딩 형식을 지정 (euc-kr)하여 해결하였다.

인코딩이 어떻게 되어 있는지 주어진 디렉터리 내의 파일을 열어 리스트에 존재하는 인코딩 방식을 적용해보고, 오류가 생기면 다음에 존재하는 인코딩 방식으로 순차적으로 열어보도록 작성하였다. 이후 엑셀의 기본 설정인 EUC-KR 인코딩으로 파일을 저장하였고, 이 파일의 목적은 파일을 분리하기 전 같은 인코딩 방식으로 통일하는 것이다.

<a id="graphing"></a>

### 3. 각각의 파일을 읽어 그래프로 나타낼 수 있는 코드를 작성한다.

<a id="web-based-file-selection"></a>

### 4. HTML 웹 기반으로 각 파일을 선택할 수 있도록 하고, 이를 3.과 연결한다.

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

## 4. 과제를 통한 고찰 (배운 점 / 느낀 점)
데이터 분석하기에 앞서 데이터의 특징이 무엇인지, 데이터의 종류가 무엇인지에 대한 인지가 선행되어야 제대로 된 데이터분석을 진행할 수 있다는 것을 더욱 실감하게 되었다. 그 데이터의 특성을 분석하는 것은 결국 사람이 직접 해야 하는 영역이고 방향성은 사람이 결정해야 하는 것을 알았다.

정부 공공 데이터 포털에서 정보를 다운받았을 때, 여러 속성이 CSV파일 내에 존재하였으나 조사기관이 서로 다른 데이터를 모두 취합한 것에 불과해서 모든 데이터가 정형화되어 존재하지 않았다. AI를 이용하여 데이터를 분석하기 전 데이터를 가공하는 과정에서 시간이 많이 소모되었는데, 위의 코드를 수정하는 시행착오의 과정에서 하나라도 데이터의 정제 및 취사선택이 진행되지 않으면 이후 데이터가 분석되지 않거나, 이상치가 출력되는 등의 결과가 나타나게 되었다. 데이터의 가공도 중요하지만 데이터를 정제하여 분석에 알맞게 쓸 수 있도록 하는 과정인 데이터 분석도 가공 못지않게 중요하거나 더 중요할 수 있겠다는 생각을 하였다.
