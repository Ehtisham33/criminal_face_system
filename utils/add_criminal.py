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
from db_utils import init_db

init_db()

add_criminal(r"D:\Glaxit Projects\criminal_face_system\known_criminals\1.jpg", "John Doe", "Mark Doe", 32, "Robbery")
add_criminal(r"D:\Glaxit Projects\criminal_face_system\known_criminals\2.jpg", "John hamza", "Mark Doe", 45, "harrasment")
add_criminal(r"D:\Glaxit Projects\criminal_face_system\known_criminals\3.jpg", "John usman", "Mark Doe", 35, "degree case")
add_criminal(r"D:\Glaxit Projects\criminal_face_system\known_criminals\4.jpg", "John sajawal", "Mark Doe", 34, "pm issue")
add_criminal(r"D:\Glaxit Projects\criminal_face_system\known_criminals\5.jpg", "John yasir", "Mark Doe", 30, "nasira issue")