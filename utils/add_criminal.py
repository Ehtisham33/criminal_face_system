from encode_face import get_face_encoding
from db_utils import add_criminal_record
from faiss_utils import add_to_index
import sys

def add_criminal(image_path, name, father_name, age, crime):
    encoding = get_face_encoding(image_path)
    if encoding is None:
        print("No face found in the image.")
        return
    criminal_id = add_criminal_record(name, father_name, age, crime)
    add_to_index(encoding, criminal_id)
    print(f"Added criminal with ID {criminal_id}")

# Example usage:
# add_criminal("known_criminals/1.jpg", "John Doe", "Mark Doe", 32, "Robbery")
