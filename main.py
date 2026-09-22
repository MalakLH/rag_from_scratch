from data import *
from chunks_in_list import store_chunks

file_name = input("Enter the name of the text file: ")
chunks_log=[]

while file_name:
    chunks_log = store_chunks(file_name, chunks_log)
    file_name = input("Enter the name of the text file (or press Enter to finish): ")

print("Chunks stored in chunks_log:", chunks_log)