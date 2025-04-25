import os
import numpy as np
import faiss
import json
from utils.encode_face import get_face_encoding

images_dir = "known_criminals/"
index = faiss.IndexFlatL2(128)
id_map = []

for filename in os.listdir(images_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(images_dir, filename)
        encoding = get_face_encoding(image_path)
        if encoding is not None:
            index.add(np.array([encoding], dtype='float32'))
            criminal_id = int(os.path.splitext(filename)[0])  # filename is "1.jpg" → ID = 1
            id_map.append(criminal_id)

faiss.write_index(index, "faiss_index/index.faiss")
with open("faiss_index/id_mapping.json", "w") as f:
    json.dump(id_map, f)

print(f"✅ Rebuilt index with {len(id_map)} criminals.")
