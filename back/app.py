from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return "Hello, this is the backend of the Bulletin Board!"

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'GET':
        return jsonify(messages)
    elif request.method == 'POST':
        data = request.get_json()
        if data and 'message' in data:
            new_message = data['message']
            messages.append(new_message)
            return jsonify({"message": new_message})
        else:
            return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

