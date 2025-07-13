import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def traduzir_texto(texto, idioma_destino):
    prompt = f"Traduza este texto para {idioma_destino}: {texto}"

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return resposta['choices'][0]['message']['content'].strip()
