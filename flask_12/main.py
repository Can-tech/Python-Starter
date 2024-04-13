from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators
from flask import request
from flask_bootstrap import Bootstrap4
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap4(app)

class MyForm(FlaskForm):
    email = StringField('email', [validators.Length(min=6, max=120), validators.Email()])
    password = StringField('password', [validators.Length(min=6, max=120), validators.DataRequired()])

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == 'GET':
        return render_template("login.html", form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if(form.email.data == "admin@mail.com" and form.password.data == "123456"):
                return render_template("success.html")
            else:
                return render_template("denied.html")
        else:
            return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
