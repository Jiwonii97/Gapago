import streamlit as st

from papago import my_papago
from voice_analysis import text_to_speaking

# 여러 문장을 받아 한줄씩 읽게 하는 함수
def read_sentense(sentense):
    for s in sentense:
        text_to_speaking([my_papago(s, "ko")], "en")
        
        
def make_newline(size):
    for _ in range(size):
        st.write("")