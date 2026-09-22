import numpy as np
from model_call import generate_embedding

def cosine_similarity(a, b):
    a = np.array(a)
    b= np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, all_chunks, top_k=5):
    query_vec = generate_embedding(query)
    scored = [
        (cosine_similarity(query_vec, chunk["vector"]), chunk)
        for chunk in all_chunks
    ]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_k]