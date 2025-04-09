import os
import requests

HF_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN") or "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"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"temperature": 0.5, "max_new_tokens": 300}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and 'generated_text' in result[0]:
            return result[0]['generated_text'].strip()
        elif isinstance(result, dict) and 'generated_text' in result:
            return result['generated_text'].strip()
        elif isinstance(result, list) and 'generated_text' not in result[0] and 'text' in result[0]:
            return result[0]['text'].strip()
        else:
            return str(result)
    except Exception as e:
        return f"❌ Hugging Face Error: {e}"