from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def homePage():
    posts = requests.get("https://api.npoint.io/aae85e7f47f4ae1acfc1").json();
    return render_template("index.html", posts=posts);

@app.route("/about")
def aboutPage():
    return render_template("about.html");

@app.route("/contact")
def contactPage():
    return render_template("contact.html");

@app.route("/post/<id>")
def postPage(id):
    arrId = int(id)-1
    post = requests.get(f"https://api.npoint.io/aae85e7f47f4ae1acfc1/{arrId}").json();
    return render_template("post.html", post=post);
    
if __name__ == "__main__":
    app.run(debug=True)