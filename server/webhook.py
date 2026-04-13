import requests
import json

webhook_url = 'http://127.0.0.1:4040/webhook'

data = {'name' : 'tiiya',
        'Channel URL' : 'Test URL'}

r = requests.post(webhook_url, data = json.dumps(data), headers={'Content-Type' : 'application/json'})