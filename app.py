import os
from flask import Flask, render_template, jsonify
import requests
import random

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        # 처음에 잘 됐던 영어 성경 API
        res = requests.get("https://bible-api.com/john 3:16")
        data = res.json()
        
        # 유튜브는 일단 가장 안전한 거 하나만!
        return jsonify({
            "verse": data['text'],
            "ref": data['reference'],
            "youtube_id": "wM7id6NTo68" 
        })
    except:
        return jsonify({
            "verse": "For God so loved the world...",
            "ref": "John 3:16",
            "youtube_id": "wM7id6NTo68"
        })

if __name__ == '__main__':
    app.run(debug=True)