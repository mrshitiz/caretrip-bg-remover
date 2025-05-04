@app.route('/remove', methods=['POST'])
def remove_bg():
    try:
        file = request.files['image']
        input_image = Image.open(file.stream)
        img_io = io.BytesIO()
        input_image.save(img_io, 'JPEG', quality=90)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
    except Exception as e:
        return str(e), 500
