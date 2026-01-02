import os
from flask import Flask, render_template, jsonify
import requests
import random

# [수정포인트] 현재 파일이 있는 위치를 절대 경로로 잡아서 Flask한테 알려주기
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

HYMN_LIST = ["M_Tj730I-vA", "8X8W9_vH2vA", "r-99uH9vC_w", "wM7id6NTo68"]

@app.route('/')
def home():
    # 여기서 에러나면 파일이 진짜 없는거임!
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        res = requests.get("https://bible-api.com/?random=verse")
        bible_data = res.json()
        return jsonify({
            "verse": bible_data['text'],
            "ref": bible_data['reference'],
            "youtube_id": random.choice(HYMN_LIST)
        })
    except:
        return jsonify({"verse": "데이터 가져오기 실패!", "ref": "ㅠㅠ", "youtube_id": ""})

if __name__ == '__main__':
    app.run(debug=True)