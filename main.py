import os
import pickle

from data import *
from chunks_in_list import store_chunks
from model_call import generate_embedding


file_name = input("Enter the name of the text file: ")
chunks_log=[]

while file_name:
    chunks_log = store_chunks(file_name, chunks_log)
    file_name = input("Enter the name of the text file (or press Enter to finish): ")

print("Chunks stored in chunks_log:", chunks_log)

cache_file = "embeddings.pkl"

if os.path.exists(cache_file):
    # Load vectors directly from your hard drive (takes 0.01 seconds)
    with open(cache_file, "rb") as f:
        all_chunks = pickle.load(f)
    print("Loaded cached embeddings from disk!")
else:
    # Generate vectors via OpenRouter API (takes minutes)
    all_chunks = [generate_embedding(chunk) for chunk in chunks_log]
    
    # Save for next time
    with open(cache_file, "wb") as f:
        pickle.dump(all_chunks, f)