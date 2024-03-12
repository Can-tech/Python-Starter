from flask import Flask, render_template
import random
import time
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    random_num = random.randint(1,10)
    current_time = time.localtime().tm_year
    return render_template("index.html", random_num=random_num, copyright_year=current_time)

@app.route("/guess/<name>")
def guess_page(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()
    age_response = requests.get(f"https://api.agify.io?name={name}").json()
    return render_template("guess.html", gender=gender_response["gender"], age=age_response["age"])
    
@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_posts = requests.get("https://api.npoint.io/c319e93f118fb066adc5").json()
    return render_template("blog.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)