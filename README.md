# cliente_gpt_oss_internet.py
import requests

# Substitua pelo IP público ou URL do VPS/Render
API_URL = "http://SEU_IP_OU_URL:5000/api/chat"

def chamar_gpt_oss(prompt, modelo="gpt_oss_120b"):
    payload = {"model": modelo, "prompt": prompt}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return response.json()["resposta"]
        else:
            return f"Erro {response.status_code}: {response.text}"
    except Exception as e:
        return f"Falha na requisição: {e}"

# === Exemplo de uso ===
if __name__ == "__main__":
    prompt = "Explique aprendizado de máquina de forma simples."
    print("GPT-OSS 20B:", chamar_gpt_oss(prompt, "gpt_oss_20b"))
    print("GPT-OSS 120B:", chamar_gpt_oss(prompt, "gpt_oss_120b"))
