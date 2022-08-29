import streamlit as st
import numpy as np
import cv2

# user defined function
from papago import my_papago, google_trans
from my_easyocr import my_easy_ocr
from check_korean import len_lang
from voice_analysis import speaking_to_text, text_to_speaking
from util import read_sentense, make_newline

# 결과 출력 조작 변수
flag = False

# flag 설정
def is_upload_img(img):
    global flag
    if img != None:
        flag = True
    else:
        flag = False
        
# 사이드바를 통해 데이터 작업 진행

# 메인 이미지
st.sidebar.image("asserts/question.png", width=180)
st.sidebar.markdown("# GAPAGO")

sidebar_radio = st.sidebar.radio("", ["이미지 번역", "텍스트 번역", "음성 번역"])

# >>> 1. 이미지 번역
if sidebar_radio == "이미지 번역":
    # 헤드라인
    st.title("이미지로 번역을 진행해보자!")
    st.markdown("이미지를 업로드하여 해당 이미지의 텍스트를 번역해보자!!")
    st.markdown("한글이 포함된 이미지를 업로드 하면 영문으로 번역해줍니다..")
    st.markdown("---")
    
    # 이미지 업로드
    text_image = st.file_uploader(
        label = "이미지를 선택해주세요...", 
        type = ["jpg", "png", "jpeg"]
    )
    btn_click = st.button("번 역", on_click = is_upload_img(text_image))
    
    if flag:
        # 이미지 출력창
        file_bytes = np.asarray(
            bytearray(text_image.read()), 
            dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # 문장 추출
        box_img, sentense = my_easy_ocr(opencv_image)
        st.image(box_img, channels = "BGR")
        
        # 개행
        make_newline(2)
        
        # 텍스트 출력 부분
        col0_1, col0_2 = st.columns(2)
        
        # 원문
        with col0_1:     
            # 원본 데이터 출력
            st.write("< 원  문 >")
            
            # 문장 출력
            for s in sentense:
                st.write(s)
            
            # 음성으로 듣기
            st.button("원 문 듣 기",
                    on_click = lambda : text_to_speaking(sentense))
        
        # 번역본
        with col0_2:            
            # 원본 데이터 출력
            st.write("< 번  역 >")
            
            # 텍스트 번역 결과
            for s in sentense:
                st.write(my_papago(s, "ko"))
                
            # 음성으로 듣기
            st.button("번 역 듣 기",
                        on_click=lambda: read_sentense(sentense))
                
    else:
        # 번역 진행이 되지 않은 경우
        st.image("asserts/no_image.jpg", width = 240)
        st.error("이미지를 업로드 해주세요!!!")
    
# >>> 2.텍스트 번역 
# 조건 선택에 따른 출력 수정
elif sidebar_radio == "텍스트 번역":
    # 헤드라인
    st.title("텍스트로 번역을 진행해보자!")
    st.markdown("영어를 입력하면 한글로 번역시켜줍니다")
    st.markdown("---")
    
    # 텍스트 입력
    base_sentense = st.text_area(
            label = "텍스트를 입력하세요..",
            height = 320,           # 입력 박스 높이
            max_chars = 2000,
            help = "번역을 진행할 텍스트를 입력해주세요",
            placeholder="한글로 입력하시면 영어로 번역해드립니다" # 처음에 입력 설명
        )
    
    # 텍스트가 입력된 경우만 번역 진행
    if base_sentense:
        kr_lang, en_lang = len_lang(base_sentense)
        if (en_lang > kr_lang) and kr_lang > 0:
            st.write(google_trans(base_sentense))
        else:
            st.write(my_papago(base_sentense))
    else:
        st.write("아직 번역이 진행되지 않았습니다...")
        
        
# >>> 3. 음성 번역
# 조건 선택에 따른 출력 수정
elif sidebar_radio == "음성 번역":
    
    # 헤드라인
    st.title("음성을 인식하여 번역을 진행해보자!")
    st.markdown("한국어로 음성 인식을 시켜 영어로 번역해보자!!")
    st.markdown("---")
    
    col01, col02 = st.columns([2,10])
    with col01:
        voice_input = st.button("음 성 인 식")
    with col02:
        # 버튼을 클릭한 경우
        st.write("#### :point_left: \t버튼을 누르고 번역을 원하는 문장을 말해보세요")
    
    make_newline(3)
    
    if voice_input:
        col1, col2 = st.columns(2, gap="large")
        
        # 원본 데이터 출력
        with col1:
            texts = speaking_to_text()           
            st.markdown("#### <   인식된 문장   >")
            make_newline(2)
            st.write(texts)
        
        with col2:
            st.markdown("#### <   번역한 문장   >")
            make_newline(2)
            st.write(my_papago(texts, "kr"))
            
            # 자동으로 읽어주기
            text_to_speaking([my_papago(texts, "kr")], lang="en")