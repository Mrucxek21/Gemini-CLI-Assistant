from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# To wypisze listę WSZYSTKICH modeli dostępnych dla Twojego klucza
for m in client.models.list(config={"page_size": 100}):
    print(m.name)