import re

# 한국어가 있는가
def isKorean(text):
    hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  
    english = re.compile('[a-zA-Z]+')  
    result_hangul = hangul.findall(text)
    result_english = english.findall(text)
    return True if len(result_hangul) > len(result_english) else False

# 영어만 있는가
def onlyEnglish(text): 
    hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  
    english = re.compile('[a-zA-Z]+')  
    result_hangul = hangul.findall(text)
    result_english = english.findall(text)
    return True if len(result_english) > 0 and len(result_hangul) == 0 else False

# 각 언어의 corpus 개수 확인
def len_lang(text):
    hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  
    english = re.compile('[a-zA-Z]+')  
    result_hangul = hangul.findall(text)
    result_english = english.findall(text)
    return len(result_hangul), len(result_english)