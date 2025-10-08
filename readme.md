🤖 LLM Code Explainer (Gemini API)
Project Overview
This is a minimal, proof-of-concept Python application designed to explain code snippets using Google's Gemini large language model (LLM) via the official google-genai SDK.

The project demonstrates:

Secure integration with a major LLM provider (Google Gemini).

Use of System Instructions for robust prompt engineering.

Utilization of environment variables for API key security (best practice).

Robust error handling for production-grade stability.

Prerequisites
Before running the application, ensure you have the following:

Python 3.9+ installed. (You've already set this up on your MacBook M4).

A Gemini API Key from Google AI Studio.

A working virtual environment for dependency management.

Setup and Installation
Follow these steps to set up the project locally.

1. Clone the Repository (or navigate to your directory)
Bash

# Assuming you are in the parent directory
cd openai-explainer
2. Activate the Virtual Environment
Ensure your virtual environment is active before installing dependencies.

Bash

source venv/bin/activate
3. Install Dependencies
Install the necessary Python SDK for the Gemini API.

Bash

pip install google-genai
4. Configure Your API Key 🔑 (Crucial Step!)
For security, the application reads the key from an environment variable.

In your terminal, set the GEMINI_API_KEY variable. This command saves the key to your shell profile (.zshrc) so it persists across terminal sessions.

Bash

echo 'export GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
⚠️ Replace YOUR_GEMINI_API_KEY_HERE with the actual key you obtained from Google AI Studio.

Usage
Run the script directly from your terminal, passing the code snippet you want explained as a command-line argument enclosed in single quotes.

Example 1: Recursive Function
Bash

python3 explainer_gemini.py 'def factorial(n): return 1 if n == 0 else n * factorial(n-1)'
Example 2: Simple Dictionary
Bash

python3 explainer_gemini.py 'data = {"name": "Alice", "age": 30}; print(data.get("name"))'
Code Structure
The main logic resides in explainer_gemini.py.

Key Components
File/Function	Description
explainer_gemini.py	The main script containing the API logic.
explain_code()	Function that encapsulates the Gemini API call.
model='gemini-2.5-flash'	The specific model used for fast, capable text generation.
system_instruction	Used to define the model's persona (expert engineer) and output format (bullet points).
try...except blocks	Includes specific error handling for ResourceExhaustedError (rate limiting) and APIError.

Export to Sheets
Error Handling
The script implements robust error checking to provide clear user feedback if the API call fails due to common issues:

API Key Missing/Invalid: Will fail on client initialization or return an APIError.

Rate Limit Exceeded: Will explicitly catch and report a ResourceExhaustedError.

Network Issues: Caught by the general Exception block.