from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'API is running.'

@app.route('/remove', methods=['POST'])
def remove_bg():
    return 'Image received!', 200

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
