import urllib.request
import urllib
import json
from googletrans import Translator

# 파파고 번역 함수
def my_papago(input_text, lang = "en"):
    # 키값 불러오기
    # client = { client_id, client_secret }
    with open("keys.json", "r") as f:
        client = json.load(f)

    url = "https://openapi.naver.com/v1/papago/n2mt"

    # 입력할 텍스트 데이터
        
    encText = urllib.parse.quote(input_text, encoding="utf-8")

    # 번역을 진행할 언어가 영어 <-> 한국어 인지 확인
    if lang == "en":
        start, end = "en", "ko"
    else:
        start, end = "ko", "en"
        
    # 데이터 요청
    data = f"source={start}&target={end}&text={encText}"
    request = urllib.request.Request(url)

    # PAPAGO API 계정 로그린
    request.add_header("X-Naver-Client-Id",client["papago_api_key"]["client_id"])
    request.add_header("X-Naver-Client-Secret",client["papago_api_key"]["client_secret"])

    # url 호출
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    # API 호출 결과
    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body)
        
        translated_text = data["message"]["result"]["translatedText"]
    # 에러 발생
    else:
        print("Error Code:" + rescode)
        
    return translated_text

# 구글 번역 함수
def google_trans(texts):
    
    translator = Translator()
    res = translator.translate(texts, dest="ko").text
    
    return res