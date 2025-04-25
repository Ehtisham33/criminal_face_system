from utils.encode_face import get_face_encoding
from utils.faiss_utils import search_encoding
from utils.db_utils import get_criminal_by_id

def detect_criminal(image_path):
    encoding = get_face_encoding(image_path)
    if encoding is None:
        print("No face found.")
        return
    criminal_id = search_encoding(encoding)
    if criminal_id:
        info = get_criminal_by_id(criminal_id)
        print("⚠️ Criminal Detected!")
        print(f"ID: {info[0]}, Name: {info[1]}, Father: {info[2]}, Age: {info[3]}, Crime: {info[4]}")
    else:
        print("✅ No criminal match found.")

# Example:
detect_criminal(r"uploads\0.jpg")
