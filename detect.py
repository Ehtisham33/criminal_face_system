from flask import Flask, request, jsonify
from utils.encode_face import get_face_encoding
from utils.faiss_utils import search_encoding
from utils.db_utils import get_criminal_by_id
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/detect', methods=['POST'])
def detect_criminal_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    encoding = get_face_encoding(image_path)
    if encoding is None:
        return jsonify({'message': 'No face found'}), 200

    criminal_id = search_encoding(encoding)
    if criminal_id:
        info = get_criminal_by_id(criminal_id)
        return jsonify({
            'status': 'Criminal Detected',
            'id': info[0],
            'name': info[1],
            'father': info[2],
            'age': info[3],
            'crime': info[4]
        }), 200
    else:
        return jsonify({'status': 'No criminal match found'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7004,debug=True)
