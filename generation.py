
import os

from openai import OpenAI

from search import search


def answer_question(query, all_chunks):
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPEN_ROUTER_KEY"),
    )
    results = search(query, all_chunks, top_k=5)
    context = "\n\n---\n\n".join([r[1]["text"] for r in results])

    prompt = f"""Answer the question using ONLY the context below. 
If the context doesn't contain the answer, say so.

Context:
{context}

Question: {query}
"""
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content