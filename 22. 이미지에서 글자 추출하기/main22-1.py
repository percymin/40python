from PIL import Image
import pytesseract

image_path = r"22. 이미지에서 글자 추출하기\한국말 캡쳐.png"
# 이미지 저장경로

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#tesseract 다운받은곳 경로
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")
#이미지에서 한글을 찾아 추출

print(text)
#한글을 찾아 추출한거에서 출력