import faiss
import numpy as np
import json
import os

INDEX_PATH = "faiss_index/index.faiss"
ID_MAP_PATH = "faiss_index/id_mapping.json"

def load_index():
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(ID_MAP_PATH, 'r') as f:
            id_map = json.load(f)
    else:
        index = faiss.IndexFlatL2(128)
        id_map = []
    return index, id_map

def save_index(index, id_map):
    faiss.write_index(index, INDEX_PATH)
    with open(ID_MAP_PATH, 'w') as f:
        json.dump(id_map, f)

def add_to_index(encoding, criminal_id):
    index, id_map = load_index()
    index.add(np.array([encoding], dtype='float32'))
    id_map.append(criminal_id)
    save_index(index, id_map)

def search_encoding(encoding, top_k=1):
    index, id_map = load_index()
    if index.ntotal == 0:
        return None
    D, I = index.search(np.array([encoding], dtype='float32'), top_k)
    best_match_index = I[0][0]
    return id_map[best_match_index]
