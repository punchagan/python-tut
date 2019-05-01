import random


def cows_n_bulls(number, guess):
    total = 0
    for digit in guess:
        count = number.count(digit)
        total = total + count

    bulls = 0
    for digit in guess:
        if number.count(digit) != 0:
            if number.index(digit) == guess.index(digit):
                bulls = bulls + 1

    cows = total - bulls
    return cows, bulls


def string_to_number(x):
    guess = []
    for digit in list(x):
        guess.append(int(digit))
    return guess


def generate_random():
    number = []
    while len(number) < 4:
        digit = random.randint(0, 9)
        if number.count(digit) == 0:
            number.append(digit)
    return number


if __name__ == "__main__":
    number = generate_random()
    bulls = 0
    while bulls < 4:
        x = input("Please enter a 4-digit number: ")
        guess = string_to_number(x)
        cows, bulls = cows_n_bulls(number, guess)

        print("Bulls:", bulls)
        print("Cows:", cows)

    print("Congratulations!")
