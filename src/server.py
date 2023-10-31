from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        messages.append(message)
        return jsonify({'status': 'Message sent successfully'})
    return jsonify({'status': 'Message not sent'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    tmpmessages = messages[:]
    messages.clear()
    return jsonify({'messages': tmpmessages})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
