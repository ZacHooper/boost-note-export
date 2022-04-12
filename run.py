from json import load
import requests
import json
from os import environ
from dotenv import load_dotenv
load_dotenv()

auth = f"Bearer {environ.get('API_KEY')}"

r = requests.get("https://boostnote.io/api/docs", headers={'Authorization': auth})
data = r.json()

with open('boostnote_data.json', 'w') as outfile:
    outfile.write(json.dumps(data))

