from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')  # 👈 IMPORTANTE

result = ocr.ocr(r"C:\Users\cchum\Downloads\image1.jpg")

if result and result[0]:
    for line in result[0]:
        text = line[1][0]
        conf = line[1][1]
        print(text, conf)
else:
    print("No se detectó texto")