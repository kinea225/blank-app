
# #문서작성하기 ----------------------------------------------
# import streamlit as st

# st.title("🎈 안녕하세요")

# st.header("1. 기본 텍스트 출력")

# st.write("이것은 st.write()를 사용한 텍스트입니다.")
# st.text("이것은 형식 없는 텍스트입니다.")

# st.markdown("**굵은 글씨**와 *기울임 글씨* 사용하기")
# st.markdown("> 인용구 스타일")

# st.code("""
# def hello():
#     print("hello, Streamlit!")        
# """,language='python')

# st.header("2 표 출력")
# import pandas as pd
# df = pd.DataFrame({
#     "이름": ["홍길동","이몽룡"],
#     "나이":[29,34]
# })

# st.dataframe(df)

# st.header("3. 이미지 출력")

# st.image("https://i.namu.wiki/i/4El7Omx8MUNbvgPh06rSi50cTR5HI9QF3x8KuRAibfxEj6z-3Yqo19bi7pFUwyo73MaFIyibjmyibkq3Z8yzuXfFpPZ4siVz_OjZhEsyDmlSc6sb4Bq5OFsqW28zfqBWKgg5pVqwTIt4tcB6vjVR_Q.webp", width=300)


# #데이터 표현하기 ----------------------------------------------
# import streamlit as st
# st.set_page_config(page_title="문서 작성 예제", layout="centered")

# # 제목
# st.title("📘 Streamlit 문서 작성 예제")

# # 섹션
# st.header("1. 기본 텍스트 출력")

# # 표 출력
# st.header("2. 표 출력")
# import pandas as pd
# df = pd.DataFrame({
#     "이름": ["홍길동", "이몽룡"],
#     "나이": [29, 34]
# })
# st.dataframe(df)

# #데이터 입력받기 ----------------------------------------------

# #ex1)
# import streamlit as st
# import datetime

# name = st.text_input("이름을 입력하세요")
# age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
# birthdate = st.date_input("생년월일 선택")
# hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
# agree = st.checkbox("이용 약관에 동의합니다")
# file = st.file_uploader("파일 업로드")

# if st.button("제출"):
#     st.success(f"{name}님({age}세), 제출 완료!")

# #ex2)
# import streamlit as st

# st.title("📋 사용자 정보 입력 폼")

# # 1. 사용자 입력 위젯
# name = st.text_input("🧑 이름을 입력하세요")
# age = st.number_input("🎂 나이를 입력하세요", min_value=0, max_value=120, step=1)
# gender = st.radio("🚻 성별을 선택하세요", ["남자", "여자", "기타"])
# interests = st.multiselect("💡 관심 있는 주제를 선택하세요", ["인공지능", "데이터 분석", "웹 개발", "금융", "디자인"])
# description = st.text_area("📘 자기소개 또는 하고 싶은 말")
# agree = st.checkbox("✅ 개인정보 수집 및 이용에 동의합니다")

# # 2. 제출 버튼
# if st.button("제출"):
#     if not name:
#         st.warning("이름을 입력하세요.")
#     elif not agree:
#         st.error("개인정보 수집 동의가 필요합니다.")
#     else:
#         # 3. 결과 출력
#         st.success("입력이 완료되었습니다! 🎉")
#         st.markdown("---")
#         st.subheader("📄 제출 내용 요약")
#         st.write(f"**이름:** {name}")
#         st.write(f"**나이:** {age}세")
#         st.write(f"**성별:** {gender}")
#         st.write(f"**관심 주제:** {', '.join(interests) if interests else '없음'}")
#         st.write("**소개글:**")
#         st.info(description if description else "작성하지 않음")

# #데이터 입력받기 ----------------------------------------------
# #ex1)
# import streamlit as st
# import datetime

# name = st.text_input("이름을 입력하세요")
# age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
# birthdate = st.date_input("생년월일 선택")
# hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
# agree = st.checkbox("이용 약관에 동의합니다")
# file = st.file_uploader("파일 업로드")

# if st.button("제출"):
#     st.success(f"{name}님({age}세), 제출 완료!")

# #ex2)
# import streamlit as st

# st.title("📋 사용자 정보 입력 폼")

# # 1. 사용자 입력 위젯
# name = st.text_input("🧑 이름을 입력하세요")
# age = st.number_input("🎂 나이를 입력하세요", min_value=0, max_value=120, step=1)
# gender = st.radio("🚻 성별을 선택하세요", ["남자", "여자", "기타"])
# interests = st.multiselect("💡 관심 있는 주제를 선택하세요", ["인공지능", "데이터 분석", "웹 개발", "금융", "디자인"])
# description = st.text_area("📘 자기소개 또는 하고 싶은 말")
# agree = st.checkbox("✅ 개인정보 수집 및 이용에 동의합니다")

# # 2. 제출 버튼
# if st.button("제출"):
#     if not name:
#         st.warning("이름을 입력하세요.")
#     elif not agree:
#         st.error("개인정보 수집 동의가 필요합니다.")
#     else:
#         # 3. 결과 출력
#         st.success("입력이 완료되었습니다! 🎉")
#         st.markdown("---")
#         st.subheader("📄 제출 내용 요약")
#         st.write(f"**이름:** {name}")
#         st.write(f"**나이:** {age}세")
#         st.write(f"**성별:** {gender}")
#         st.write(f"**관심 주제:** {', '.join(interests) if interests else '없음'}")
#         st.write("**소개글:**")
#         st.info(description if description else "작성하지 않음")


# #레이아웃 columns ----------------------------------------------

# import streamlit as st

# col1,col2 = st.columns([2,3])
# # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

# with col1 :
#   # column 1 에 담을 내용
#   st.title('여기는 1 열 ')
# with col2 :
#   # column 2 에 담을 내용
#   st.title('여기는 2열')
#   st.checkbox('2열 체크박스 1 ')


# # with 구문 말고 다르게 사용 가능 
# col1.subheader(' 1열 서브헤더 !! ')

# col2.checkbox('2열 체크박스 2 ') 

# #=>위에 with col2: 안의 내용과 같은 기능을합니다

# #레이아웃 Tap ----------------------------------------------

# import streamlit as st

# # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
# tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

# with tab1:
#   #tab A 를 누르면 표시될 내용
#   st.write('hello')

# with tab2:
#   #tab B를 누르면 표시될 내용 
#   st.write('hi')

# #레이아웃 sidebar ----------------------------------------------
# import streamlit as st

# #st.sidebar는 

# st.sidebar.title('this is sidebar')
# st.sidebar.checkbox('체크박스에 표시될 문구')
# # 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 

# #레이아웃 Expander ----------------------------------------------
# import streamlit as st

# st.title("📂 Streamlit Expander 예제")

# # 예제 1: 간단한 설명 숨기기
# with st.expander("🔍 설명 보기"):
#     st.write("""
#         이 애플리케이션은 사용자의 입력을 기반으로 데이터를 필터링하고 시각화합니다.
#         아래의 항목들을 입력하면 실시간으로 결과가 변경됩니다.
#     """)

# # 예제 2: 여러 줄 텍스트 입력 숨기기
# with st.expander("✍️ 메모 입력"):
#     note = st.text_area("여기에 학습 내용을 메모하세요")

# # 예제 3: 데이터프레임 숨기기 ----------------------------------------------

# import pandas as pd

# df = pd.DataFrame({
#     "과목": ["수학", "영어", "과학"],
#     "점수": [90, 85, 95]
# })
# with st.expander("점수표 보기"):
#     st.dataframe(df)

# #레이아웃 Contatiner ----------------------------------------------
# import streamlit as st

# st.title("📦 Streamlit Container 예제")

# # 컨테이너 1 - 요약 영역
# with st.container():
#     st.subheader("1️⃣ KPI 요약")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("매출", "₩120,000")
#     col2.metric("주문", "58건")
#     col3.metric("고객 수", "34명")

# # 구분선
# st.markdown("---")

# # 컨테이너 2 - 필터 + 표 영역
# with st.container():
#     st.subheader("2️⃣ 필터링 & 데이터")

#     # 사이드 필터 (예시)
#     category = st.selectbox("카테고리 선택", ["전체", "전자", "가구", "사무"])

#     # 샘플 데이터 출력
#     import pandas as pd
#     df = pd.DataFrame({
#         "제품명": ["노트북", "책상", "펜"],
#         "카테고리": ["전자", "가구", "사무"],
#         "매출": [100000, 20000, 3000]
#     })

#     if category != "전체":
#         df = df[df["카테고리"] == category]

#     st.dataframe(df)

# # 컨테이너 3 - 하단 메모
# with st.container():
#     st.subheader("3️⃣ 메모 작성")
#     st.text_area("학습 또는 회의 메모를 입력하세요")

# #레이아웃 Empty ----------------------------------------------

# import streamlit as st

# placeholder = st.empty()

# if st.button("누르면 바뀜"):
#     placeholder.success("버튼이 눌렸습니다!")
# else:
#     placeholder.warning("아직 버튼을 누르지 않았어요.")


# #레이아웃 작성 예제
# import streamlit as st

# # --- 사이드바 (슬라이더) ---
# st.sidebar.title("슬라이더")
# slider_val = st.sidebar.slider("값 선택", 0, 2000, 1000)

# # --- 탭 구성 ---
# tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

# with tab1:
#     st.write("탭 01 내용")

#     # 2x2 레이아웃 구성
#     col1, col2,col5 = st.columns(3)
#     with col1:
#         st.markdown("### 🧱 레이아웃 01")
#         st.info(f"슬라이더 값: {slider_val}")
#     with col2:
#         st.markdown("### 🧱 레이아웃 02")
#         st.success("오른쪽 상단 영역")

#     col3, col4, col6 = st.columns(3)
#     with col3:
#         st.markdown("### 🧱 레이아웃 03")
#         st.warning("왼쪽 하단 영역")
#     with col4:
#         st.markdown("### 🧱 레이아웃 04")
#         st.error("오른쪽 하단 영역")

# with tab2:
#     st.write("탭 02 내용")

# with tab3:
#     st.write("탭 03 내용")

# #데이터 입력 받기 - select box -----------------------------------------
# import streamlit as st
# users = [{"id": 1, "name": "홍길동"}, {"id": 2, "name": "이몽룡"}]
# selected_user = st.selectbox(
#     "사용자 선택",
#     users,
#     format_func=lambda x: f"{x['name']} (ID: {x['id']})"
# )
# st.write("선택한 사용자 ID:", selected_user['id'])

# # 데이터 입력 받기 - multi select -----------------------------------------
# # ex1)
# import streamlit as st

# fruits = ["🍎 사과", "🍌 바나나", "🍇 포도", "🍑 복숭아"]

# selected_fruits = st.multiselect("좋아하는 과일을 모두 선택하세요", fruits, default=["🍎 사과"])

# st.write("당신이 선택한 과일:", selected_fruits)

# #ex2)
# import streamlit as st
# import pandas as pd

# # 예시용 간단한 데이터프레임 생성
# data = {
#     "행정구역": ["서울특별시", "부산광역시", "제주특별자치도", "서울특별시", "부산광역시"],
#     "인구수": [9500000, 3400000, 670000, 9600000, 3450000],
#     "연도": ["2024", "2024", "2024", "2025", "2025"]
# }
# df = pd.DataFrame(data)

# # 멀티셀렉트: 유저가 선택할 지역 목록
# 행정구역목록 = sorted(df["행정구역"].unique())

# # 멀티셀렉트 위젯
# selected_regions = st.multiselect(
#     "분석할 지역을 선택하세요", 
#     options=행정구역목록, 
#     default=["서울특별시"]
# )

# # 선택된 지역에 따라 필터링
# filtered_df = df[df["행정구역"].isin(selected_regions)]

# # 결과 출력
# st.write("선택된 지역 데이터:")
# st.dataframe(filtered_df)

# # 데이터 입력 받기 - radio -----------------------------------------
# #ex1)
# import streamlit as st

# gender = st.radio("성별을 선택하세요", ["남자", "여자"])
# st.write("선택한 성별:", gender)

# #ex2)
# import streamlit as st

# color = st.radio(
#     "좋아하는 색을 고르세요",
#     options=["빨강", "파랑", "초록"],
#     index=1  # 기본 선택은 "파랑"
# )
# st.success(f"선택한 색상: {color}")


# # 데이터 입력 받기 - slider -----------------------------------------
# # ex1)
# import streamlit as st

# age = st.slider("나이를 선택하세요", min_value=10, max_value=80, value=30, step=5)
# st.write("선택한 나이:", age)

# # ex2)
# import streamlit as st
# year_range = st.slider("연도 범위", min_value=2010, max_value=2025, value=(2015, 2023))
# st.write("선택한 연도:", year_range)

# # 그 외 데이터 입력 받기 -----------------------------------------------
# # 한 줄 텍스트 text_input
# import streamlit as st
# name = st.text_input("이름을 입력하세요")
# st.write("입력한 이름:", name)
# # 여러줄 텍스트 text_area -----------------------------------------------
# memo = st.text_area("메모를 입력하세요", height=150)
# st.write("입력한 메모:", memo)
# # 숫자 number_input -----------------------------------------------------
# age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)
# st.write("입력한 나이:", age)
# # 날짜 date_input
# birthdate = st.date_input("생일을 선택하세요")
# st.write("선택한 날짜:", birthdate)
# # 표 형식 데이터 data_editor -----------------------------------------------
# import pandas as pd

# df = pd.DataFrame({
#     "이름": ["홍길동", "김철수"],
#     "나이": [30, 25]
# })

# edited_df = st.data_editor(df)
# st.write("수정된 데이터:")
# st.dataframe(edited_df)

# # 파일 업로더 file_uploader ------------------------------------------------
# uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df)

# #plotly_chart -------------------------------------------------------------
# import streamlit as st
# import plotly.express as px
# import pandas as pd

# # 샘플 데이터
# df = pd.DataFrame({
#     "과일": ["사과", "바나나", "체리", "사과", "바나나", "체리"],
#     "판매량": [10, 15, 8, 12, 18, 6],
#     "지점": ["서울", "서울", "서울", "부산", "부산", "부산"]
# })

# # plotly 그래프 생성
# fig = px.bar(df, x="과일", y="판매량", color="지점", barmode="group", title="과일별 판매량")

# # Streamlit에 출력
# st.plotly_chart(fig, use_container_width=True)

# #map -------------------------------------------------------------
# # ex1) 
# # 열이름이 반드시 필요
# import streamlit as st
# import pandas as pd

# # 서울 명소 위치
# data = pd.DataFrame({
#     'lat': [37.5665, 37.5700, 37.5796],
#     'lon': [126.9780, 126.9920, 126.9770],
#     'place': ['시청', '동대문', '경복궁']
# })

# st.map(data)

# # ex2)
# import streamlit as st
# import pandas as pd
# import pydeck as pdk

# # 데이터 정의 (서울 주요 지점 예시)
# data = pd.DataFrame({
#     'lat': [37.5665, 37.5700, 37.5796],
#     'lon': [126.9780, 126.9920, 126.9770],
#     'place': ['시청', '동대문', '경복궁']
# })

# # pydeck으로 고급 지도 시각화
# st.pydeck_chart(pdk.Deck(
#     map_style='mapbox://styles/mapbox/light-v9',  # 지도 스타일
#     initial_view_state=pdk.ViewState(
#         latitude=37.5665,     # 초기 중심 위도
#         longitude=126.9780,   # 초기 중심 경도
#         zoom=11,              # 줌 레벨
#         pitch=45              # 기울기
#     ),
#     layers=[
#         pdk.Layer(
#             'ScatterplotLayer',
#             data=data,
#             get_position='[lon, lat]',  # 열 이름 주의!
#             get_color='[200, 30, 0, 160]',  # 빨간색 마커
#             get_radius=300,  # 반경
#             pickable=True,
#         )
#     ],
#     tooltip={"text": "{place}"}
# ))


# # session_state --------------------------------------------------
# import streamlit as st

# # 초기값 설정
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# # 버튼 누르면 값 증가
# if st.button("클릭하세요"):
#     st.session_state.count += 1

# # 출력
# st.write("클릭한 횟수는 ", st.session_state.count, "번 입니다.")

# # cache ----------------------------------------------------------

# # @ cache_data 데이터 처리 중심 함수
# # 파일 캐싱
# import streamlit as st
# import pandas as pd

# @st.cache_data
# def load_csv(file_path):
#     df = pd.read_csv(file_path)
#     return df

# # 호출 시 처음만 읽고 이후 캐시
# df = load_csv("my_data.csv")
# st.dataframe(df)

# #  API 요청 캐싱 
# import streamlit as st
# import time

# @st.cache_data
# def slow_function(x):
#     time.sleep(3)  # 시간이 오래 걸리는 작업
#     return x * 10

# result = slow_function(5)
# st.write("결과:", result)
# # @cache_resource 무거운 객체를 한 번만 생성하고 재사용
# # 머신러닝 캐싱
# import streamlit as st
# import joblib

# @st.cache_resource
# def load_model():
#     return joblib.load("model.pkl")

# model = load_model()
# prediction = model.predict([[1, 2, 3]])
# st.write(prediction)

# # 데이터베이스 연결 유지
# import streamlit as st
# import sqlite3

# @st.cache_resource
# def get_connection():
#     return sqlite3.connect("my_database.db")

# conn = get_connection()
# df = pd.read_sql("SELECT * FROM users", conn)
# st.dataframe(df)

# # proqress ------------------------------------------------------
# import streamlit as st
# import time

# st.write("진행 중입니다...")

# progress = st.progress(0)

# for i in range(101):
#     time.sleep(0.03)  # 작업 시뮬레이션
#     progress.progress(i)

# st.success("완료되었습니다!")

# # spinner ----------------------------------------------------------
# # ex1)
# import streamlit as st
# import time

# st.write("데이터를 불러옵니다...")

# with st.spinner("잠시만 기다려 주세요..."):
#     time.sleep(5)  # 실제 작업 시뮬레이션

# st.success("데이터 로딩 완료!")

# # ex2)
# import streamlit as st
# import time

# st.header("데이터 처리 진행 상황")

# with st.spinner("전체 작업 진행 중..."):
#     progress = st.progress(0)
#     status_text = st.empty()  # 텍스트 덮어쓰기 용 공간 확보

#     for i in range(5):
#         status_text.write(f"🔧 Step {i+1}/5: 데이터 준비 중...")
#         time.sleep(1)
#         progress.progress((i + 1) * 20)

# st.success("처리가 모두 끝났습니다!")
