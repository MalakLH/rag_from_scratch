from openai import OpenAI
import os

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPEN_ROUTER_KEY"),
)

response = client.embeddings.create(
    model="nvidia/llama-nemotron-embed-vl-1b-v2:free",
    input="Text you want to embed for your vector database",
)

embedding_vector = response.data[0].embedding
