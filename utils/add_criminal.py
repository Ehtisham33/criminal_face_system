# utils/add_criminal.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.arcface_model import get_face_embedding
from utils.db_utils import add_criminal_record, create_table
from utils.match_utils import load_embeddings, save_embeddings

import numpy as np

# Ensure database table exists
create_table()

def add_new_criminal(image_path, name, father_name, age, crime):
    embedding = get_face_embedding(image_path)
    if embedding is None:
        print(f" No face found in {image_path}")
        return

    # Save record in database
    criminal_id = add_criminal_record(name, father_name, age, crime)

    # Save individual embedding as {id}.npy
    encoding_dir = "encodings"
    os.makedirs(encoding_dir, exist_ok=True)
    np.save(os.path.join(encoding_dir, f"{criminal_id}.npy"), embedding)

    print(f" Criminal '{name}' added with ID {criminal_id}.")

# Example usage
if __name__ == "__main__":
    add_new_criminal("known_criminals/1.jpg", "John Doe", "Mark Doe", 32, "Robbery")
    add_new_criminal("known_criminals/2.jpg", "Hamza Khan", "Ali Khan", 45, "Harassment")
    add_new_criminal("known_criminals/3.jpg", "Usman Raza", "Tariq Raza", 35, "Fraud")
    add_new_criminal("known_criminals/4.jpg", "Sajawal Shah", "Asad Shah", 34, "Political case")
    add_new_criminal("known_criminals/5.jpg", "Yasir Khan", "Rashid Khan", 30, "Family dispute")