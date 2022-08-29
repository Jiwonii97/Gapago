import pyttsx3
import speech_recognition as sr

def text_to_speaking(messages, lang = "ko"):
    engine = pyttsx3.init()
    
    if lang == "en":
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    
    for message in messages:
        engine.say(message)
    engine.runAndWait()         # 없으면 tts 실행 안됨
    

def speaking_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.8         # 특정 시간동안
        said = r.listen(source)     # 마이크를 켜둠
        try:
            q = r.recognize_google(said, language="ko")
            return q
        except sr.UnknownValueError:
            return "error"
        except:
            return "error"
    
# text_to_speaking(["이제 STT가 준비가 되었습니다.", "a", "b", "c", "d", "e", "f"])
# print(speaking_to_text())