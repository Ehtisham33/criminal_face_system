from flask import Flask, request, jsonify
import os
import sys

# Append current directory to path for module access
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.arcface_model import get_face_embedding, load_model
from utils.match_utils import find_match

app = Flask(__name__)

# Upload directory
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load face recognition model at startup
load_model()

@app.route('/detect', methods=['POST'])
def detect_criminal_api():
    # Check if image file is in the request
    if 'image' not in request.files:
        return jsonify({ 'error': 'No image file provided' }), 400

    # Save uploaded image
    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Get face embedding
    embedding = get_face_embedding(image_path)
    if embedding is None:
        return jsonify({ 'criminal': False }), 200

    # Run face matching logic
    criminal_id, similarity = find_match(embedding)

    # Respond with True if match found, else False
    return jsonify({ 'criminal': criminal_id is not None }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7009, debug=True)
