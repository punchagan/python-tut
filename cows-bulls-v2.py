import random

number = []
while len(number) < 4:
    digit = random.randint(0, 9)
    if number.count(digit) == 0:
        number.append(digit)

bulls = 0
while bulls < 4:
    x = input("Please enter a 4-digit number: ")
    guess = []
    for digit in list(x):
        guess.append(int(digit))

    total = 0
    for digit in guess:
        count = number.count(digit)
        total = total + count

    bulls = 0
    for digit in guess:
        if number.count(digit) != 0:
            if number.index(digit) == guess.index(digit):
                bulls = bulls + 1

    print("Bulls:", bulls)
    print("Cows:", total - bulls)

print("Congratulations!")
