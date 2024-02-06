from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return  "<b>"+function()+"</b>"
    return wrapper

def make_emphesis(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper

def make_underlinded(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
    '<p>hey this is a paragraph!</P>' \
    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzJvdWV6M2IzNzhtenMyNnZkbDY4eXo1b3RmcXFqbW0wOTg4a210aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hFmIU5GQF18Aw/giphy.gif" width="400px"/>'

@app.route("/bye")
@make_bold
@make_emphesis
@make_underlinded
def bye():
    return "BYE !"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
