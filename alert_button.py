import time
import requests
import RPi.GPIO as GPIO
import os
from dotenv import load_dotenv #import the load_dotenv function

load_dotenv() #tell Python to look at the env.file
BOT_TOKEN = os.getenv("BOT_TOKEN") # get the BOT_TOKEN environment variable
CHAT_ID = os.getenv("CHAT_ID") #get the CHAT_ID enviroment variable
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button! Sending Telegram notification...")
            
            
            payload = { "chat_id": CHAT_ID, "text": "The Grinding Wheel"
            }
            
            
            try:
                response = requests.post(TELEGRAM_URL, data=payload)
                if response.status_code == 200:
                    print("¡Mensaje de Telegram enviado con éxito!")
                else:
                    print(f"Error al enviar: {response.status_code} - {response.text}")
            except Exception as e:
                print(f"Error de red: {e}")
                
            button_pressed = True
            
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
            
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()

