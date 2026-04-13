import requests
import json

webhook_url = 'https://predominatingly-dodecahedral-wilma.ngrok-free.dev/webhook'

data = {
    'name' : 'Tiiyaa',
    'university' : 'KMITLLLL'
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-type' : 'application/json'})

print(r)
print(r.status_code)
print(r.text)

