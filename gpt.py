#!/usr/bin/env python3
# filepath: gpt.py

import sys
import argparse
import os
import json
from openai import OpenAI

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Send inputs to ChatGPT for analysis.')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env variable)')
    parser.add_argument('--error-file', help='File containing stderr output to analyze')
    parser.add_argument('params', nargs='*', help='Additional parameters to analyze')
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OpenAI API key is required. Use --api-key or set OPENAI_API_KEY environment variable.", 
              file=sys.stderr)
        return 1
    
    # Read standard input if available
    stdin_data = sys.stdin.read() if not sys.stdin.isatty() else ""
    
    # Read error file if provided
    stderr_data = ""
    if args.error_file:
        try:
            with open(args.error_file, 'r') as f:
                stderr_data = f.read()
        except Exception as e:
            print(f"Error reading error file: {e}", file=sys.stderr)
    
    # Prepare data for analysis
    input_data = {
        "stdin": stdin_data,
        "stderr": stderr_data,
        "params": args.params
    }
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    try:
        # Send to ChatGPT for analysis
        response = client.chat.completions.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are an expert analyzer. Examine the provided input and offer insights."},
                {"role": "user", "content": f"Please analyze this data:\n{json.dumps(input_data, indent=2)}"}
            ]
        )
        
        # Print the response
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())