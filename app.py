import os
from flask import Flask, render_template, jsonify, make_response
import random
import time

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

# bible.txt 읽기
def load_bible():
    if os.path.exists('bible.txt'):
        with open('bible.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return ["항상 기뻐하라 - 데살로니가전서 5:16"]

BIBLE_LINES = load_bible()
# 절대 안 죽는 유튜브 ID (가장 대중적인 것들)
HYMN_LIST = ["wM7id6NTo68", "BySTFpGvX9k", "68vU_W3AByE", "DCPv_I63rlo", "vAnOxl_W1fQ"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    line = random.choice(BIBLE_LINES)
    if " - " in line:
        verse, ref = line.split(" - ")
    else:
        verse, ref = line, "말씀"
    
    # [치트키] 브라우저한테 "이거 매번 새로운 거니까 저장하지마!"라고 신호 보냄
    response = make_response(jsonify({
        "verse": verse,
        "ref": ref,
        "youtube_id": random.choice(HYMN_LIST)
    }))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response