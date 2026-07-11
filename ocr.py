from flask import Flask, request, jsonify
from paddleocr import PaddleOCR
import numpy as np
import cv2

app = Flask(__name__)

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en',
    use_gpu=False,
    show_log=False,
    det_db_box_thresh=0.3,
    det_db_unclip_ratio=1.8
)

@app.route("/ocr", methods=["POST"])
def ocr_image():

    file = request.files["image"]
    campo = request.form["campo"]

    image_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    result = ocr.ocr(img, cls=True)

    text = []

    for line in result[0]:
        text.append(line[1][0])

    return jsonify({
        "campo": campo,
        "valor": " ".join(text)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)