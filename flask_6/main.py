from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts_raw = requests.get("https://api.npoint.io/c319e93f118fb066adc5")
    posts=blog_posts_raw.json()
    return render_template("index.html", posts=posts)

@app.route("/post/<id>")
def post(id):
    blog_posts_raw = requests.get("https://api.npoint.io/c319e93f118fb066adc5")
    posts=blog_posts_raw.json()
    filtered_post = {}
    for post in posts:
        if(post["id"]==int(id)):
            filtered_post=post
    return render_template("post.html", post=filtered_post)


if __name__ == "__main__":
    app.run(debug=True)
