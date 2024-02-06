from flask import Flask
import random
app=Flask(__name__)

rnd_num = random.randint(0,9)

@app.route("/")
def ask():
    return "<h1>Guess 0 - 9 :</h1>" \
    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzQxM2UxM3ZzaHF2YzQxOGwyYmcwOGZucTN1azA4bGgzeXBiNTcweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/glJdAXojfP3wPEg84a/giphy.gif' />" \
    ""
@app.route("/<int:route_num>")
def check(route_num):
    global rnd_num
    if(route_num < rnd_num):
        return "<h3>Pls, choose higher !</h3>"
    elif(route_num > rnd_num):
        return "<h3>Pls, choose lower !</h3>"
    else:

        rnd_num = random.randint(0,9)
        return "<h3>Correct, Good Job !</h3>"


if(__name__=="__main__"):
    app.run(debug=True)