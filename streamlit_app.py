import random

import streamlit as st

st.set_page_config(page_title="영단어 & BTS", page_icon="🎵", layout="centered")

WORDS = [
    ("학교", "school"),
    ("사과", "apple"),
    ("행복한", "happy"),
    ("책", "book"),
    ("친구", "friend"),
    ("집", "home"),
    ("강아지", "dog"),
    ("고양이", "cat"),
    ("먹다", "eat"),
    ("달리다", "run"),
    ("크다", "big"),
    ("작다", "small"),
    ("배우다", "learn"),
    ("공원", "park"),
    ("바다", "sea"),
    ("좋아하다", "like"),
    ("놀다", "play"),
    ("도와주다", "help"),
    ("감사하다", "thank"),
    ("비", "rain"),
    ("해", "sun"),
    ("달", "moon"),
]


def start_new_game():
    st.session_state.score = 0
    st.session_state.question_count = 0
    st.session_state.feedback = ""
    st.session_state.show_answer = False
    st.session_state.pending_new_question = True


def next_question():
    st.session_state.pending_new_question = True
    st.session_state.feedback = ""
    st.session_state.show_answer = False


def check_answer():
    user_answer = st.session_state.get("answer_input", "").strip().lower()
    correct_answer = st.session_state.current_word[1].lower()

    if user_answer == correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = "정답입니다! 👏"
        st.session_state.question_count += 1
        st.session_state.pending_new_question = True
        st.session_state.show_answer = False
    else:
        st.session_state.feedback = f"아쉽네요. 정답은 {st.session_state.current_word[1]}입니다."
        st.session_state.show_answer = True
        st.session_state.question_count += 1


if "score" not in st.session_state:
    start_new_game()

if st.session_state.get("pending_new_question", False):
    st.session_state.pending_new_question = False
    st.session_state.current_word = random.choice(WORDS)
    st.session_state.answer_input = ""
    st.session_state.feedback = ""
    st.session_state.show_answer = False

st.title("📚 영어 공부 + BTS")
st.write("영단어 게임도 하고 BTS도 알아보세요.")

word_tab, bts_tab = st.tabs(["영단어", "BTS 소개"])

with word_tab:
    st.subheader("영단어 게임")
    st.write("한국어 뜻을 보고 영어 단어를 맞혀 보세요.")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("점수", st.session_state.score)
    with col2:
        st.metric("푼 문제", st.session_state.question_count)

    st.subheader("문제")
    st.write(f"뜻: {st.session_state.current_word[0]}")

    with st.form("answer_form"):
        st.text_input("영어 단어를 입력하세요.", key="answer_input")
        submitted = st.form_submit_button("정답 확인")

    if submitted:
        check_answer()

    if st.session_state.feedback:
        if "정답" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    if st.session_state.show_answer:
        if st.button("다음 문제"):
            next_question()
    else:
        if st.button("새 게임"):
            start_new_game()

with bts_tab:
    st.subheader("BTS 소개")
    st.write("BTS는 방탄소년단으로, 한국의 대표적인 보이그룹입니다.")
    st.info("멤버: RM, 진, 슈가, 제이홉, 지민, 뷔, 정국")

    st.write("BTS는 음악과 춤으로 많은 사람들에게 사랑받고 있습니다.")
    st.write("대표곡: Dynamite, Butter, Boy With Luv")

    st.markdown("- RM: 그룹을 이끄는 리더")
    st.markdown("- 진: 차분하고 멋진 분위기")
    st.markdown("- 슈가: 빠른 랩과 감성")
    st.markdown("- 제이홉: 에너지 넘치는 메인댄서")
    st.markdown("- 지민: 섬세한 춤과 매력")
    st.markdown("- 뷔: 우아하고 특별한 분위기")
    st.markdown("- 정국: 강한 보컬과 열정")
