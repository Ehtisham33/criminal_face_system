# utils/match_utils.py

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

EMBEDDINGS_PATH = "encodings/embeddings.npy"
IDS_PATH = "encodings/ids.npy"

def save_embeddings(embeddings, ids):
    np.save(EMBEDDINGS_PATH, embeddings)
    np.save(IDS_PATH, ids)

def load_embeddings():
    if os.path.exists(EMBEDDINGS_PATH) and os.path.exists(IDS_PATH):
        embeddings = np.load(EMBEDDINGS_PATH)
        ids = np.load(IDS_PATH)
        return embeddings, ids
    else:
        return np.empty((0, 512)), np.array([])

def find_match(query_embedding, threshold=0.45):
    embeddings, ids = load_embeddings()
    if len(embeddings) == 0:
        return None, None

    similarities = cosine_similarity([query_embedding], embeddings)[0]
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]

    if best_score >= threshold:
        return int(ids[best_idx]), float(best_score)
    else:
        return None, None
