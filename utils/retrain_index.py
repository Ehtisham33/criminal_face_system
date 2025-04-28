# utils/retrain_index.py

import os
import numpy as np
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.match_utils import save_embeddings

def retrain_index():
    encoding_dir = "encodings"
    embeddings = []
    ids = []

    for filename in os.listdir(encoding_dir):
        if filename.endswith(".npy") and filename not in ["embeddings.npy", "ids.npy"]:
            embedding_path = os.path.join(encoding_dir, filename)
            embedding = np.load(embedding_path)
            if embedding.shape[0] != 512:
                continue  # skip wrong sized embeddings
            embeddings.append(embedding)
            criminal_id = int(os.path.splitext(filename)[0])
            ids.append(criminal_id)

    if len(embeddings) == 0:
        print("❌ No individual embeddings found.")
        return

    embeddings = np.vstack(embeddings)
    save_embeddings(embeddings, ids)
    print(f"✅ Index retrained with {len(ids)} embeddings.")

if __name__ == "__main__":
    retrain_index()
