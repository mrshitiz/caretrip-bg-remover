from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'API is running.'

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    file = request.files['image']
    input_image = Image.open(file.stream)
    output_image = remove(input_image)

    white_bg = Image.new("RGBA", output_image.size, "WHITE")
    white_bg.paste(output_image, (0, 0), output_image)
    img_io = io.BytesIO()
    white_bg.convert("RGB").save(img_io, 'JPEG', quality=95)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
