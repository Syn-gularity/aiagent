import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions

def main():
    load_dotenv("./gemini.env")

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """

    args = sys.argv
    if len(args) < 2:
        raise Exception('No Questions! Use python3 main.py "Your Ai Prompt" [--verbose]')
    user_prompt = args[1]
    verbose = False
    if len(args) > 2 and args[2] == "--verbose":
        verbose = True
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    # Handling the AI Response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if response.function_calls != None:
        for function_call_part in response.function_calls:
            print(function_call_part)
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Normal Response:")
        print(response.text)
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()