from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from posts import get_posts, add_post

app = Flask(__name__)

# Load biến môi trường từ file .env
load_dotenv()

# Ví dụ sử dụng các biến môi trường (thay bằng cấu hình Firebase nếu cần)
project_id = os.getenv("PROJECT_ID")
client_email = os.getenv("CLIENT_EMAIL")
print("Project ID:", project_id)
print("Client Email:", client_email)

@app.route("/", methods=["GET"])
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/", methods=["POST"])
def add():
    title = request.form["title"]
    content = request.form["content"]
    add_post(title, content)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
