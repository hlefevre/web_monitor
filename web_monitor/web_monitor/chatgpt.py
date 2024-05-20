from openai import OpenAI
from web_monitor.config import CHATGPT_ENGINE, CHATGPT_PROMPT_TEMPLATE, CHATGPT_MAX_TOKENS, CHATGPT_TEMPERATURE

def generate_summary(content, api_key):
    """
    Utilise l'API de ChatGPT pour générer une synthèse du contenu.
    
    :param content: Contenu à synthétiser.
    :param api_key: Clé API de ChatGPT.
    :return: Synthèse générée par ChatGPT.
    """
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model=CHATGPT_ENGINE,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": CHATGPT_PROMPT_TEMPLATE.format(content=content)}
        ],
        max_tokens=CHATGPT_MAX_TOKENS,
        temperature=CHATGPT_TEMPERATURE
    )
    
    return response.choices[0].message.content.strip()