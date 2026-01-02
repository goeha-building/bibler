import os
from flask import Flask, render_template, jsonify
import requests
import random

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# 찬송가 리스트 (형님이 좋아하는 유튜브 ID 더 추가해도 됨!야르 ㅋㅋㅋㅋㅋㅋㅋ)
# 검증된 '퍼가기 허용' 찬송가 ID 리스트
HYMN_LIST = [
    "wM7id6NTo68", # 손경민 - 행복 (Official)
    "BySTFpGvX9k", # 시간을 뚫고 (Welove)
    "68vU_W3AByE", # 꽃들도 (JWorship)
    "DCPv_I63rlo", # 원하고 바라고 기도합니다
    "vAnOxl_W1fQ"  # 은혜
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        # 한글 성경 API (대한성서공회 개역개정 느낌으로 가져오기)
        # 0은 창세기, 1은 출애굽기... 랜덤으로 장/절을 가져오는 무료 API입니다.
        res = requests.get("https://v0.bible/api/ko/gaesun/random")
        data = res.json()
        
        return jsonify({
            "verse": data['content'],
            "ref": f"{data['book_name']} {data['chapter']}:{data['verse']}",
            "youtube_id": random.choice(HYMN_LIST)
        })
    except:
        return jsonify({
            "verse": "마음이 지친 당신에게 평안이 있기를.",
            "ref": "위로의 말씀 1:1",
            "youtube_id": random.choice(HYMN_LIST)
        })

if __name__ == '__main__':
    app.run(debug=True)