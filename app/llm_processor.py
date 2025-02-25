import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def structure_data(content, user_schema):
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""Extract data from below website content to match this JSON schema.
    Fill values where possible, leave null if not found. Return ONLY valid JSON:

    Schema: {user_schema}
    
    Content: {content}"""
    
    response = model.generate_content(prompt)
    
    # Basic validation
    try:
        return json.loads(response.text)
    except:
        return {"error": "Invalid JSON response", "raw_output": response.text}