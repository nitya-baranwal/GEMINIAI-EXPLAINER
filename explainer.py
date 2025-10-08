# explainer.py
import os
from openai import OpenAI
import sys

# 1. API Client Initialization
# The client automatically picks up the OPENAI_API_KEY
# from the environment variable (thanks to the setup in Step 2!)
try:
    client = OpenAI()
except Exception as e:
    print("Error: Could not initialize OpenAI client.")
    print("Please ensure your OPENAI_API_KEY environment variable is set correctly.")
    print(f"Details: {e}")
    sys.exit(1)


def explain_code(code_snippet):
    """
    Makes a direct API call to the OpenAI Chat Completion endpoint.
    """
    print("🤔 Sending code to OpenAI for explanation...")

    # 2. Direct API Request (The core of the project!)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # A fast and capable model for this task
            messages=[
                {"role": "system", "content": "You are an expert software engineer. Your job is to explain a provided code snippet in clear, plain, and concise English. Use bullet points and focus on what the code does, not just line-by-line syntax."},
                {"role": "user", "content": f"Explain this code:\n\n---\n{code_snippet}\n---"},
            ],
            temperature=0.2  # Lower temperature for factual, less creative output
        )

        # 3. Extracting the Response
        explanation = response.choices[0].message.content
        return explanation

    except Exception as e:
        return f"🚨 An API error occurred: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python explainer.py 'your code snippet here'")
        print("Example: python explainer.py 'def fib(n): return fib(n-1) + fib(n-2) if n > 1 else n'")
        sys.exit(1)

    # Joins all command-line arguments into a single string
    code_to_explain = " ".join(sys.argv[1:])

    result = explain_code(code_to_explain)

    print("\n" + "="*50)
    print("✨ CODE EXPLANATION ✨")
    print("="*50)
    print(result)
    print("="*50)