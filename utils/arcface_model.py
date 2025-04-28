# utils/arcface_model.py

from insightface.app import FaceAnalysis
import cv2

app = None

def load_model():
    global app
    if app is None:
        app = FaceAnalysis(name='buffalo_l')  # High accuracy ArcFace model
        app.prepare(ctx_id=0, det_size=(640, 640))

def get_face_embedding(image_path):
    global app
    if app is None:
        load_model()

    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Error reading image: {image_path}")
        return None

    faces = app.get(img)
    if len(faces) == 0:
        return None

    return faces[0].embedding
