
# #문서작성하기
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


# #데이터 표현하기
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

# #데이터 입력받기

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

# #데이터 입력받기
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


# #레이아웃 columns
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

# #레이아웃 Tap
# import streamlit as st

# # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
# tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

# with tab1:
#   #tab A 를 누르면 표시될 내용
#   st.write('hello')

# with tab2:
#   #tab B를 누르면 표시될 내용 
#   st.write('hi')

# #레이아웃 sidebar
# import streamlit as st

# #st.sidebar는 

# st.sidebar.title('this is sidebar')
# st.sidebar.checkbox('체크박스에 표시될 문구')
# # 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 

# #레이아웃 Expander
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

# # 예제 3: 데이터프레임 숨기기

# import pandas as pd

# df = pd.DataFrame({
#     "과목": ["수학", "영어", "과학"],
#     "점수": [90, 85, 95]
# })
# with st.expander("점수표 보기"):
#     st.dataframe(df)

# #레이아웃 Contatiner
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

# #레이아웃 Empty

# import streamlit as st

# placeholder = st.empty()

# if st.button("누르면 바뀜"):
#     placeholder.success("버튼이 눌렸습니다!")
# else:
#     placeholder.warning("아직 버튼을 누르지 않았어요.")


#레이아웃 작성 예제
import streamlit as st

# --- 사이드바 (슬라이더) ---
st.sidebar.title("슬라이더")
slider_val = st.sidebar.slider("값 선택", 0, 2000, 50)

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

with tab1:
    st.write("탭 01 내용")

    # 2x2 레이아웃 구성
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧱 레이아웃 01")
        st.info(f"슬라이더 값: {slider_val}")
    with col2:
        st.markdown("### 🧱 레이아웃 02")
        st.success("오른쪽 상단 영역")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧱 레이아웃 03")
        st.warning("왼쪽 하단 영역")
    with col4:
        st.markdown("### 🧱 레이아웃 04")
        st.error("오른쪽 하단 영역")

with tab2:
    st.write("탭 02 내용")

with tab3:
    st.write("탭 03 내용")

