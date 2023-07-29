from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MongoDB에 연결
client = MongoClient('mongodb://mongodb1:27017,mongodb2:27017/')
db = client['bulletin_board']
collection = db['messages']

@app.route('/')
def index():
    return "게시판"

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'GET':
        # MongoDB에서 메시지 가져오기
        messages = list(collection.find({}, {'_id': 0}))
        return jsonify(messages)
    elif request.method == 'POST':
        data = request.get_json()
        if data and 'message' in data:
            new_message = data['message']
            # 새로운 메시지를 MongoDB에 저장
            collection.insert_one({'message': new_message})
            return jsonify({"message": new_message})
        else:
            return jsonify({"error": "잘못된 요청입니다."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

