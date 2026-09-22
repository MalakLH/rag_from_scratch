import os
import pickle

from data import *
from chunks_in_list import store_chunks
from model_call import generate_embedding
from generation import answer_question


file_name = input("Enter the name of the text file: ")
chunks_log=[]

while file_name:
    chunks_log = store_chunks(file_name, chunks_log)
    file_name = input("Enter the name of the text file (or press Enter to finish): ")

print("Chunks stored in chunks_log:", chunks_log)

cache_file = "embeddings.pkl"

if os.path.exists(cache_file):
    # Load chunks + vectors directly from disk
    with open(cache_file, "rb") as f:
        all_chunks = pickle.load(f)
    print("Loaded cached embeddings from disk!")
else:
    print("Generating embeddings via OpenRouter...")
    all_chunks = []
    
    for chunk in chunks_log:
        # 1. Generate vector (ensuring chunk is a string)
        text_content = chunk["text"] if isinstance(chunk, dict) else chunk
        vector = generate_embedding(text_content)
        
        # 2. Save vector alongside the original text
        all_chunks.append({
            "text": text_content,
            "vector": vector
        })
    
    # 3. Save the combined list to disk
    with open(cache_file, "wb") as f:
        pickle.dump(all_chunks, f)
        
    print(f"Successfully embedded and cached {len(all_chunks)} chunks!")

query = input("Enter your query: ")
response=answer_question(query, all_chunks)
print("Response:", response)