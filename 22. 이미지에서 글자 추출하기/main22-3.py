from PIL import Image
import pytesseract

image_path = r"22. 이미지에서 글자 추출하기\한국말 캡쳐.png"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")
#한국말 캡쳐파일 문자로 추출
print(text)

with open(r"22. 이미지에서 글자 추출하기\한글변환.txt", "w", encoding="utf8") as f:
    f.write(text)
#한글변환 파일 생성