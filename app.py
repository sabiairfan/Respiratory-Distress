from flask import Flask, render_template, request
import os
import numpy as np
import cv2

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
EYE_FOLDER = 'eyes'

os.makedirs(EYE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    # Read uploaded file into OpenCV image
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if img is None:
        return "Invalid image", 400

    # Save the uploaded eye directly in eyes folder
    eye_path = os.path.join(EYE_FOLDER, 'uploaded_eye.png')
    cv2.imwrite(eye_path, img)

    return f"Eye image saved at {eye_path}"





if __name__ == "__main__":
    app.run(debug=True)
