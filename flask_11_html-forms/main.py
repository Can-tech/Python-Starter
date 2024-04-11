from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html");

@app.route("/login", methods=["POST"])
def receive_data():
    return render_template("login.html", username=request.form['username'],password = request.form['password'] )

if __name__ == "__main__": #if the script is being run directly
    app.run(debug=True)