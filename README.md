# Gapago

> 본 서비스는 "서울ICT이노베이션스퀘어_고급언어인지과정_3기" 수업과정 중 제출한 과제물 입니다
---

## 실행 방법
``` streamlit run main.py``` 

## 서비스 설명
streamlit을 활용한 세가지 버젼의 번역 사이트를 만들었습니다
  <br/>
<h2>1.이미지 번역<h2/>
<img src = "./asserts/example_translation1.PNG" width="80%" height="80%">
<h5>easyocr을 활용하여 이미지 파일을 업로드 하면 해당 이미지의 텍스트를 분석해 box가 추가된 이미지가 결과로 나오게 됩니다. <h5/> 
<h5>이후 인식한 텍스트와 이를 번역한 텍스트가 나오고 하단의 버튼을 통해 tts(text-to-speaking) 서비스를 동시에 받을 수 있습니다.<h5/>  
  <br/>
> easyocr 깃허브 : https://github.com/JaidedAI/EasyOCR
<br/>
<br/>
<br/>  
<h2> 2. 텍스트 번역 <h2/>
<img src = "./asserts/example_translation2.PNG" width="80%" height="80%">
<h5>PAPAGO API와 Googletrans API를 사용하여 한글을 입력하면 해당 텍스트에 대한 번역 결과를 출력해주는 번역 서비스 입니다.<h5/>
<br/>
<br/>
<br/>
<h2>3. 음성 번역<h2/>
<img src = "./asserts/example_translation3.PNG" width="80%" height="80%">
<h5>버튼을 누르고 번역을 원하는 음성을 말하면 해당 음성을 인식해 한글->영문으로 번역을 진행하고 해당 결과의 tts 서비스를 받을 수 있습니다. <h5/>
<br/>
<br/>
  
---
  <br/>
<h2>개발기간
  <h3>2022/07/01 ~ 2022/08/30 (2개월)<h3/>
    <h5>- 22/07/01 ~ 22/07/08 : 서비스 개발 기획 (번역 웹서비스 구현)<h5/>
    <h5>- 22/07/09 ~ 22/07/15 : OCR 서비스 사전조사 (Tesseract OCR, EasyOCR, GoogleTrans, etx.)<h5/>
    <h5>- 22/07/16 ~ 22/07/25 : EasyOCR 모델 학습 및 성능 분석<h5/>
    <h5>- 22/07/25 ~ 22/08/10 : EasyOCR 모델을 적용하여 유저 서비스 개발<h5/>
    <h5>- 22/08/10 ~ 22/08/15 : 웹페이지 디자인 및 세부 서비스 개발/구현<h5/>
    <h5>- 22/08/16 ~ 22/08/30 : 이미지/텍스트/음성 번역 서비스 구현 및 개발<h5/>
    <h5>- 22/08/30 ~ 22/09/01 : 서비스 확인 및 오류 수정<h5/>
<h2/>
