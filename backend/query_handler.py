import ollama

def query_deepseek(prompt):
    response = ollama.chat("deepseek-r1", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
