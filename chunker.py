def chunk_text(text, chunk_size=200):
    # naive: split by paragraph, then group paragraphs until ~chunk_size chars
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) > chunk_size and current:
            chunks.append(current)
            current = p
        else:
            current += "\n\n" + p if current else p
    if current:
        chunks.append(current)
    return chunks