import requests
import time

url = "https://cvflorentcramettedata.streamlit.app/"  # Remplace par ton URL

while True:
    try:
        response = requests.get(url)
        print(f"Ping {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"Erreur : {e}")
    time.sleep(600)  # Ping toutes les 10 minutes
