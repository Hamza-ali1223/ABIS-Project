import requests
from stt import voice_assistant

url = "http://localhost:5678/webhook/voice"

while True:
    text=voice_assistant()

    data = {"text": text}

    response = requests.post(url, json=data)

    print("Status:", response.status_code)
    print("Response:", response.text)


# this is a demo of our n8n agent that drafts emails, makes calender events
# and also communicates