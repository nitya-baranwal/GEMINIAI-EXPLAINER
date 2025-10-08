# explainer_gemini.py
import os
import sys
from google import genai
from google.genai import types

# 1. API Client Initialization
# The client automatically picks up the GEMINI_API_KEY
# from the environment variable (thanks to the setup in Step 1!)
try:
    client = genai.Client()
except Exception as e:
    print("Error: Could not initialize Gemini client.")
    print("Please ensure your GEMINI_API_KEY environment variable is set correctly.")
    print(f"Details: {e}")
    sys.exit(1)


def explain_code(code_snippet):
    """
    Makes a direct API call to the Google Gemini Chat Completion endpoint
    with robust error handling.
    """
    print("🤔 Sending code to Gemini for explanation...")

    system_instruction = "You are an expert software engineer. Your job is to explain a provided code snippet in clear, plain, and concise English. Use bullet points and focus on what the code does, not just line-by-line syntax."
    prompt_text = f"Explain this code:\n\n---\n{code_snippet}\n---"

    # 2. Direct API Request (The core of the project!)
    try:
        # Define the core instruction for the model
        # system_instruction = "You are an expert software engineer. Your job is to explain a provided code snippet in clear, plain, and concise English. Use bullet points and focus on what the code does, not just line-by-line syntax."

        # Construct the full prompt
        # prompt_text = f"Explain this code:\n\n---\n{code_snippet}\n---" 

        # 2. Direct API Request (The core of the project!)
        response = client.models.generate_content(
            model='gemini-2.5-flash',  # A fast and capable model for this task
            contents=prompt_text,     # PASS THE PROMPT TEXT DIRECTLY HERE
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.2
            )
        )

        # 3. Extracting the Response
        explanation = response.text
        return explanation

    except ResourceExhaustedError:
        # Catches 429 errors (Too Many Requests/Rate Limit) or quota issues
        return "🚨 ERROR: API Rate Limit Exceeded or Quota reached. Please try again later or check your Gemini usage dashboard."
    
    except APIError as e:
        # Catches general API issues (e.g., invalid model name, authentication failures)
        return f"🚨 API ERROR: A General API Error occurred: {e}"

    except Exception as e:
        # Catches all other unexpected errors (e.g., network issues, local exceptions)
        return f"🚨 UNEXPECTED ERROR: An unexpected issue occurred: {type(e).__name__} - {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 explainer_gemini.py 'your code snippet here'")
        print("Example: python3 explainer_gemini.py 'def fib(n): return fib(n-1) + fib(n-2) if n > 1 else n'")
        sys.exit(1)

    # Joins all command-line arguments into a single string
    code_to_explain = " ".join(sys.argv[1:])

    result = explain_code(code_to_explain)

    print("\n" + "="*50)
    print("✨ CODE EXPLANATION (via Gemini) ✨")
    print("="*50)
    print(result)
    print("="*50)