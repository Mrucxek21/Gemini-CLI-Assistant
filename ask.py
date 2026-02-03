import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: Dont find GEMINI_API_KEY in .env file")
    sys.exit(1)

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("Use: python ask.py 'Your question here'")
        return
    
    prompt = " ".join(sys.argv[1:])
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",  #    <-- here u can change model name
            contents=prompt
        )
        
        print("\nGemini answer:")
        print("-" * 30)
        print(response.text)
        print("-" * 30)
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            print("⚠️ Query limit reached (Error 429). Please wait a moment.")
        elif "404" in error_msg:
            print(f"❌ Error 404: Model not found. run check_models.py and rename\nDetails: {e}")
        else:
            print(f"❌ Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
