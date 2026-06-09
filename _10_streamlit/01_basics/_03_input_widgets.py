import streamlit as st

st.title("🥱 Input Widgets 😪")
st.header("Button", divider = "rainbow")

# button 생성 + 입력 값 저장
clicked = st.button("Click me")
print("clicked :", clicked) # 파이썬 콘솔에 출력

if clicked == True:
    st.write("버튼이 클릭되었습니다!!!!!!!🐶")
else:
    st.write("아직 버튼을 클릭하지 않았습니다.")

# 리셋 버튼
st.button("Reset", type="primary")

# 텍스트 인풋
st.subheader("Text Input", divider = "rainbow")

destination = st.text_input(
    label = "가고싶은 여행지가 있으신가요?",
    placeholder="여행지를 입력하세요"
)

st.write("입력된 여행지 :", destination)

# text_area
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")


# 라디오 버튼 : 여러개 중 한가지만 선택
st.subheader("Radio Buttons", divider = "rainbow")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

st.subheader("", divider = "rainbow")

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

where = st.radio("당장 어디로 가고 싶은가요?",
                 [":rainbow[집]", "***집***", "집 : home"],
                 captions=['당신은 집에 가고싶다', '나는 집에 가고싶다', '너는 집에 가고싶다'])


# select box
st.header('SelectBox', divider = "rainbow")
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)
if mbti == '모름':
    st.write('당신은 :red[싸이코패스]입니다.')
else:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')

# ckeckbox
st.subheader('Checkbox', divider = "rainbow")
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")