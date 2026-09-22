import chunker

def store_chunks(file_name, chunks_log):
    with open(f'data/{file_name}.txt', 'r') as file:
        # Read the entire file
        content = file.read()

    chunks = chunker.chunk_text(content, chunk_size=200)

    for chunk in chunks:
        chunks_log.append({"text": chunk, "source": file_name})

    return chunks_log
