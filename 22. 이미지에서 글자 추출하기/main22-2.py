import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
laguages = pytesseract.get_languages(config='')
#사용가능한 언어를 확인
print(laguages)