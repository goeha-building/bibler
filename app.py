import os
from flask import Flask, render_template, jsonify
import requests
import random

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# 절대 안 죽는 전설의 찬양 리스트 (수정 버전)
HYMN_LIST = ["wM7id6NTo68", "BySTFpGvX9k", "68vU_W3AByE", "DCPv_I63rlo", "vAnOxl_W1fQ"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        # 이번엔 아주 유명한 볼트(Bolt) 성경 API를 써봅시다 (한글 개역개정)
        # 랜덤 장/절을 뽑기 위해 랜덤 파라미터를 던집니다.
        res = requests.get("https://pyonbible.vercel.app/api/ko/gaesun/random")
        data = res.json()
        
        return jsonify({
            "verse": data['content'],
            "ref": f"{data['book_name']} {data['chapter']}:{data['verse']}",
            "youtube_id": random.choice(HYMN_LIST)
        })
    except Exception as e:
        # 만약 API가 또 죽으면? 이번엔 좀 더 성경다운 '고정 말씀'을 보여줍니다.
        return jsonify({
            "verse": "수고하고 무거운 짐 진 자들아 다 내게로 오라 내가 너희를 쉬게 하리라",
            "ref": "마태복음 11:28",
            "youtube_id": random.choice(HYMN_LIST)
        })

if __name__ == '__main__':
    app.run(debug=True)