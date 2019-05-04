from flask import Flask
from cows_bulls import cows_n_bulls, string_to_number, generate_random

app = Flask(__name__)
app.number = generate_random()


@app.route("/")
def hello():
    return "Welcome to Cows and Bulls. Start playing by guessing a 4 digit number in the URL."


@app.route("/<guess>")
def c_n_b(guess):
    guess = string_to_number(guess)
    cows, bulls = cows_n_bulls(app.number, guess)
    if bulls == 4:
        app.number = generate_random()
        return "Congratulations!"
    return "%s cows, %s bulls" % (cows, bulls)


app.run(debug=True)
