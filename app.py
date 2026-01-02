import os
from flask import Flask, render_template, jsonify
import random

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# [비밀 병기] 서버가 켜질 때 bible.txt를 몽땅 읽어옵니다.
def load_bible():
    if os.path.exists('bible.txt'):
        with open('bible.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return ["항상 기뻐하라! - 데살로니가전서 5:16"] # 파일 없을 때 대비

BIBLE_LINES = load_bible()
HYMN_LIST = ["wM7id6NTo68", "BySTFpGvX9k", "68vU_W3AByE", "DCPv_I63rlo", "vAnOxl_W1fQ"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    # 3만 절이 있든 10만 절이 있든 여기서 랜덤으로 하나 픽!
    line = random.choice(BIBLE_LINES)
    
    # 보통 성경 txt는 "구절내용 - 장:절" 형식이니 대충 나눠줍니다.
    if " - " in line:
        verse, ref = line.split(" - ")
    else:
        verse, ref = line, "말씀"

    return jsonify({
        "verse": verse,
        "ref": ref,
        "youtube_id": random.choice(HYMN_LIST)
    })