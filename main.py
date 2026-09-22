import chunker
from data import *

file_name = input("Enter the name of the text file: ")

with open(f'data/{file_name}.txt', 'r') as file:
    # Read the entire file
    content = file.read()
    print(content)

chunks = chunker.chunk_text(content, chunk_size=200)
print (f"Number of chunks: {len(chunks)}")