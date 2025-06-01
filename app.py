from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://your-website-link.com"  # URL bạn muốn tạo QR
    img = qrcode.make(url)
    img_path = os.path.join('static', 'qr.png')
    img.save(img_path)
    return render_template('index.html', qr_image='qr.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
