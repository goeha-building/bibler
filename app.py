import os
from flask import Flask, render_template, jsonify
import random

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# [무적의 데이터] 서버 내부에서 바로 꺼내 쓰니까 광속입니다.
BIBLE_DATA = [
    {"verse": "For God so loved the world that he gave his one and only Son.", "ref": "John 3:16"},
    {"verse": "The Lord is my shepherd, I shall not be in want.", "ref": "Psalm 23:1"},
    {"verse": "I can do everything through him who gives me strength.", "ref": "Philippians 4:13"},
    {"verse": "In the beginning God created the heavens and the earth.", "ref": "Genesis 1:1"},
    {"verse": "Your word is a lamp to my feet and a light for my path.", "ref": "Psalm 119:105"}
]

# 검증된 유튜브 ID (유튜브 공식 채널 영상들)
HYMN_LIST = ["wM7id6NTo68", "BySTFpGvX9k", "68vU_W3AByE", "DCPv_I63rlo", "vAnOxl_W1fQ"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    selected = random.choice(BIBLE_DATA)
    return jsonify({
        "verse": selected['verse'],
        "ref": selected['ref'],
        "youtube_id": random.choice(HYMN_LIST)
    })

if __name__ == '__main__':
    app.run(debug=True)