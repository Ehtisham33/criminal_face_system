# detect.py

from flask import Flask, request, jsonify
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.arcface_model import get_face_embedding, load_model
from utils.match_utils import find_match
from utils.db_utils import get_criminal_by_id

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

load_model()

@app.route('/detect', methods=['POST'])
def detect_criminal_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    embedding = get_face_embedding(image_path)
    if embedding is None:
        return jsonify({'status': 'No face found'}), 200

    criminal_id, similarity = find_match(embedding)

    if criminal_id is not None:
        info = get_criminal_by_id(criminal_id)
        return jsonify({
            'status': 'Criminal Detected',
            'id': info[0],
            'name': info[1],
            'father_name': info[2],
            'age': info[3],
            'crime': info[4],
            'similarity': round(similarity, 4)
        }), 200
    else:
        return jsonify({'status': 'No criminal match found'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7009, debug=True)
