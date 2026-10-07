import os
from dotenv import load_dotenv
import requests

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

print("--- DIAGNÓSTICO DE CONFIGURACIÓN ---")
print(f"BOT_TOKEN leído: {bot_token}")
print(f"CHAT_ID leído: {chat_id}")

if not bot_token or not chat_id:
    print("\n❌ ERROR: No se pudieron leer las variables del archivo .env")
else:
    print("\n🔄 Probando conexión directa con Telegram...")
    # Corregido: Se agregó /bot antes del token
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "🤖 Prueba de conexión exitosa desde la Raspberry Pi."
    }
    try:
        r = requests.post(url, data=payload)
        print(f"Código de estado HTTP: {r.status_code}")
        print(f"Respuesta de Telegram: {r.text}")
    except Exception as e:
        print(f"❌ Error de red: {e}")
