'''
#문서작성하기
import streamlit as st

st.title("🎈 안녕하세요")

st.header("1. 기본 텍스트 출력")

st.write("이것은 st.write()를 사용한 텍스트입니다.")
st.text("이것은 형식 없는 텍스트입니다.")

st.markdown("**굵은 글씨**와 *기울임 글씨* 사용하기")
st.markdown("> 인용구 스타일")

st.code("""
def hello():
    print("hello, Streamlit!")        
""",language='python')

st.header("2 표 출력")
import pandas as pd
df = pd.DataFrame({
    "이름": ["홍길동","이몽룡"],
    "나이":[29,34]
})

st.dataframe(df)

st.header("3. 이미지 출력")

st.image("https://i.namu.wiki/i/4El7Omx8MUNbvgPh06rSi50cTR5HI9QF3x8KuRAibfxEj6z-3Yqo19bi7pFUwyo73MaFIyibjmyibkq3Z8yzuXfFpPZ4siVz_OjZhEsyDmlSc6sb4Bq5OFsqW28zfqBWKgg5pVqwTIt4tcB6vjVR_Q.webp", width=300)
'''
'''
#데이터 표현하기
import streamlit as st
st.set_page_config(page_title="문서 작성 예제", layout="centered")

# 제목
st.title("📘 Streamlit 문서 작성 예제")

# 섹션
st.header("1. 기본 텍스트 출력")

# 표 출력
st.header("2. 표 출력")
import pandas as pd
df = pd.DataFrame({
    "이름": ["홍길동", "이몽룡"],
    "나이": [29, 34]
})
st.dataframe(df)
'''
'''
#데이터 입력받기

#ex1)
import streamlit as st
import datetime

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
birthdate = st.date_input("생년월일 선택")
hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
agree = st.checkbox("이용 약관에 동의합니다")
file = st.file_uploader("파일 업로드")

if st.button("제출"):
    st.success(f"{name}님({age}세), 제출 완료!")

#ex2)
import streamlit as st

st.title("📋 사용자 정보 입력 폼")

# 1. 사용자 입력 위젯
name = st.text_input("🧑 이름을 입력하세요")
age = st.number_input("🎂 나이를 입력하세요", min_value=0, max_value=120, step=1)
gender = st.radio("🚻 성별을 선택하세요", ["남자", "여자", "기타"])
interests = st.multiselect("💡 관심 있는 주제를 선택하세요", ["인공지능", "데이터 분석", "웹 개발", "금융", "디자인"])
description = st.text_area("📘 자기소개 또는 하고 싶은 말")
agree = st.checkbox("✅ 개인정보 수집 및 이용에 동의합니다")

# 2. 제출 버튼
if st.button("제출"):
    if not name:
        st.warning("이름을 입력하세요.")
    elif not agree:
        st.error("개인정보 수집 동의가 필요합니다.")
    else:
        # 3. 결과 출력
        st.success("입력이 완료되었습니다! 🎉")
        st.markdown("---")
        st.subheader("📄 제출 내용 요약")
        st.write(f"**이름:** {name}")
        st.write(f"**나이:** {age}세")
        st.write(f"**성별:** {gender}")
        st.write(f"**관심 주제:** {', '.join(interests) if interests else '없음'}")
        st.write("**소개글:**")
        st.info(description if description else "작성하지 않음")
'''
