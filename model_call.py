from openai import OpenAI
import os

def generate_embedding(text):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPEN_ROUTER_KEY"),
    )

    if isinstance(text, dict):
        text = text.get("text", "")
    else:
        text = text

    response = client.embeddings.create(
        model="nvidia/llama-nemotron-embed-vl-1b-v2:free",
        input=text,
    )

    embedding_vector = response.data[0].embedding

    return embedding_vector

