import openai
import json
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_json_with_llm(text, prompt_template):
    prompt = prompt_template.replace('{{extracted_text}}', text)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        temperature=0
    )
    content = response.choices[0].message.content
    return json.loads(content)
