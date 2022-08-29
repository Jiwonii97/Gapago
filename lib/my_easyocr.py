import easyocr
import numpy as np
from PIL import ImageDraw, Image
from hanspell import spell_checker

def my_easy_ocr(img):
    results = []

    reader = easyocr.Reader(['ko'], gpu=True) # need to run only once to load model into memory
    result = reader.readtext(img)

    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)

    np.random.seed(42)
    COLORS = [255, 200, 200]         # 회색 빨간색

    # 이미지에 해당 텍스트 부분 box 처리
    for i in result :
        x = i[0][0][0]
        y = i[0][0][1]
        w = i[0][1][0] - i[0][0][0]
        h = i[0][2][1] - i[0][1][1]
        
        draw.rectangle(((x, y), (x+w, y+h)), outline=tuple(COLORS), width=2)     # 사각형 추가
        
        # 텍스트 추가 및 맞춤법 검사 도입
        base_text = i[1]
        checked_text = spell_checker.check(base_text).as_dict()["checked"]
        results.append(checked_text)

    return img, results