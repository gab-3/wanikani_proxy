from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "your-wanikani-token"

@app.route('/kanji/<kanji_char>')
def get_kanji(kanji_char):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Wanikani-Revision": "20170710",
    }
    url = f"https://api.wanikani.com/v2/kanji/{kanji_char}"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

# Deploy this to a public server
