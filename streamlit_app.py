import random

import streamlit as st

st.set_page_config(page_title="영단어 게임", page_icon="📚", layout="centered")

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

st.title("📚 중학생 영단어 게임")
st.write("한국어 뜻을 보고 영어 단어를 맞혀 보세요. 한 번에 한 문제씩 재미있게 공부해 봅시다!")

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
