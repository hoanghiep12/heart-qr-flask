from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "HEAD"])
def index():
    if request.method == "HEAD":
        return "", 200 
    # Tạo QR code
    img = qrcode.make("https://heart-qr-flask.onrender.com")  # hoặc URL của bạn

    # Đường dẫn lưu file QR vào thư mục static
    img_path = "static/qr.png"
    img.save(img_path)

    return render_template("index.html", qr_image="qr.png")