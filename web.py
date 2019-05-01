from flask import Flask
from cows_bulls import cows_n_bulls, string_to_number, generate_random

app = Flask(__name__)
app.number = generate_random()


@app.route("/<guess>")
def hello_world(guess):
    guess = string_to_number(guess)
    cows, bulls = cows_n_bulls(app.number, guess)
    if bulls == 4:
        app.number = generate_random()
        return "Congratulations!"
    return "%s cows, %s bulls" % (cows, bulls)


app.run(debug=True)
