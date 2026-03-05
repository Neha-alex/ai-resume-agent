from .config import deepseek
from .prompt_builder import build_system_prompt

def chat(message, history):
    system_prompt = build_system_prompt()
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = deepseek.chat.completions.create(model="deepseek-chat", messages=messages)
    return response.choices[0].message.content