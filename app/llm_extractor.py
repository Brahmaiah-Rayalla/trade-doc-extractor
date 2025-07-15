import openai
import json
import os

def extract_json_with_openai(text, prompt_template):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = prompt_template.replace('{{extracted_text}}', text)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        temperature=0
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("OpenAI response content is None")
    return json.loads(content)

def extract_json_with_vertexai(text, prompt_template):
    from google.cloud import aiplatform
    from vertexai.language_models import ChatModel
    PROJECT_ID = os.getenv("VERTEX_PROJECT_ID")
    LOCATION = os.getenv("VERTEX_LOCATION", "us-central1")
    MODEL = os.getenv("VERTEX_MODEL", "chat-bison")
    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    chat_model = ChatModel.from_pretrained(MODEL)
    prompt = prompt_template.replace('{{extracted_text}}', text)
    chat = chat_model.start_chat()
    response = chat.send_message(prompt)
    if response.text is None:
        raise ValueError("Vertex AI response text is None")
    return json.loads(response.text)

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

def extract_json_with_llm(text, prompt_template):
    if LLM_PROVIDER == "openai":
        return extract_json_with_openai(text, prompt_template)
    elif LLM_PROVIDER == "vertexai":
        return extract_json_with_vertexai(text, prompt_template)
    else:
        raise ImportError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
